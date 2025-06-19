from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional
from crewai import Crew, LLM
from trip_agents import TripAgents
from trip_tasks import TripTasks
import os
from dotenv import load_dotenv
from functools import lru_cache

# Load environment variables
load_dotenv()

app = FastAPI(
    title="VacAIgent API",
    description="AI-powered travel planning API using CrewAI",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TripRequest(BaseModel):
    origin: str = Field(..., 
        example="Bangalore, India",
        description="Your current location")
    destination: str = Field(..., 
        example="Krabi, Thailand",
        description="Destination city and country")
    start_date: date = Field(..., 
        example="2025-06-01",
        description="Start date of your trip")
    end_date: date = Field(..., 
        example="2025-06-10",
        description="End date of your trip")
    interests: str = Field(..., 
        example="2 adults who love swimming, dancing, hiking, shopping, local food, water sports adventures and rock climbing",
        description="Your interests and trip details")

class TripResponse(BaseModel):
    status: str
    message: str
    itinerary: Optional[str] = None
    error: Optional[str] = None

class Settings:
    def __init__(self):
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        self.SERPER_API_KEY = os.getenv("SERPER_API_KEY")
        self.BROWSERLESS_API_KEY = os.getenv("BROWSERLESS_API_KEY")

@lru_cache()
def get_settings():
    return Settings()

def validate_api_keys(settings: Settings = Depends(get_settings)):
    required_keys = {
        'GEMINI_API_KEY': settings.GEMINI_API_KEY,
        'SERPER_API_KEY': settings.SERPER_API_KEY,
        'BROWSERLESS_API_KEY': settings.BROWSERLESS_API_KEY
    }
    
    missing_keys = [key for key, value in required_keys.items() if not value]
    if missing_keys:
        raise HTTPException(
            status_code=500,
            detail=f"Missing required API keys: {', '.join(missing_keys)}"
        )
    return settings

class TripCrew:
    def __init__(self, origin, destination, date_range, interests):
        self.destination = destination
        self.origin = origin
        self.interests = interests
        self.date_range = date_range
        self.llm = LLM(model="gemini/gemini-2.0-flash")

    def run(self):
        try:
            agents = TripAgents(llm=self.llm)
            tasks = TripTasks()

            city_selector_agent = agents.city_selection_agent()
            local_expert_agent = agents.local_expert()
            travel_concierge_agent = agents.travel_concierge()

            identify_task = tasks.identify_task(
                city_selector_agent,
                self.origin,
                self.destination,
                self.interests,
                self.date_range
            )

            gather_task = tasks.gather_task(
                local_expert_agent,
                self.origin,
                self.interests,
                self.date_range
            )

            plan_task = tasks.plan_task(
                travel_concierge_agent,
                self.origin,
                self.interests,
                self.date_range
            )

            crew = Crew(
                agents=[
                    city_selector_agent, local_expert_agent, travel_concierge_agent
                ],
                tasks=[identify_task, gather_task, plan_task],
                verbose=True
            )

            result = crew.kickoff()
            # Convert CrewOutput to string and ensure it's properly formatted
            return result.raw if hasattr(result, 'raw') else str(result)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            )

@app.get("/")
async def root():
    return {
        "message": "Welcome to VacAIgent API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

@app.post("/api/v1/plan-trip", response_model=TripResponse)
async def plan_trip(
    trip_request: TripRequest,
    settings: Settings = Depends(validate_api_keys)
):
    # Validate dates
    if trip_request.end_date <= trip_request.start_date:
        raise HTTPException(
            status_code=400,
            detail="End date must be after start date"
        )

    # Format date range
    date_range = f"{trip_request.start_date} to {trip_request.end_date}"

    try:
        trip_crew = TripCrew(
            trip_request.origin,
            trip_request.destination,
            date_range,
            trip_request.interests
        )
        
        itinerary = trip_crew.run()
        
        # Ensure itinerary is a string
        if not isinstance(itinerary, str):
            itinerary = str(itinerary)
            
        return TripResponse(
            status="success",
            message="Trip plan generated successfully",
            itinerary=itinerary
        )
    
    except Exception as e:
        return TripResponse(
            status="error",
            message="Failed to generate trip plan",
            error=str(e)
        )

@app.get("/api/v1/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
