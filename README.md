

A multi-agent travel planner powered by CrewAI that automates end-to-end trip planning from destination selection to day-by-day itineraries.

## Overview

TripPlanner-AgenticAI uses three specialized AI agents to plan your perfect trip:
- **City Selection Expert**: Analyzes destinations based on weather, events, and costs
- **Local Expert**: Discovers hidden gems and local insights
- **Travel Concierge**: Creates detailed day-by-day itineraries with budget breakdowns

## Features

- 🤖 Multi-agent workflow using CrewAI
- 🌐 Real-time web search and content extraction
- 📱 Multiple interfaces: Streamlit UI, FastAPI, and CLI
- 💰 Automated budget calculations
- 📋 Structured markdown itinerary output
- 🔄 Live agent execution logs

## Tech Stack

- **Language**: Python
- **Agent Framework**: CrewAI
- **LLM**: Gemini 2.0 Flash
- **Tools**: Serper.dev (search), Browserless (web scraping), Custom calculator
- **Interfaces**: Streamlit, FastAPI, CLI
- **Dependencies**: See `requirements.txt`

## Setup & Installation

### Prerequisites
- Python 3.8+
- API Keys for:
  - Gemini API
  - Serper.dev
  - Browserless

### 1. Clone Repository
```bash
git clone https://github.com/somanathdiksangi/TripPlanner-AgenticAI
cd TripPlanner-AgenticAI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
SERPER_API_KEY=your_serper_api_key_here
BROWSERLESS_API_KEY=your_browserless_api_key_here
```

## How to Run

### Option 1: Streamlit UI (Interactive)
```bash
streamlit run streamlit_app.py
```
Open http://localhost:8501 in your browser and fill out the trip planning form.

### Option 2: FastAPI (REST API)
```bash
uvicorn api_app:app --reload
```
- API docs: http://localhost:8000/docs
- Health check: http://localhost:8000/api/v1/health

#### Sample API Request
```bash
curl -X POST "http://localhost:8000/api/v1/plan-trip" \
     -H "Content-Type: application/json" \
     -d '{
       "origin": "Bangalore, India",
       "destination": "Krabi, Thailand", 
       "start_date": "2025-06-01",
       "end_date": "2025-06-10",
       "interests": "2 adults who love swimming, hiking, local food, water sports"
     }'
```

### Option 3: CLI (Command Line)
```bash
python cli_app.py \
  --origin "Bangalore, India" \
  --destination "Krabi, Thailand" \
  --start-date 2025-06-01 \
  --end-date 2025-06-10 \
  --interests "2 adults who love swimming, hiking, local food, water sports"
```

## Project Structure
```
TripPlanner-AgenticAI/
├── api_app.py              # FastAPI server
├── cli_app.py              # Command-line interface
├── streamlit_app.py        # Streamlit web UI
├── trip_agents.py          # CrewAI agents definition
├── trip_tasks.py           # CrewAI tasks definition
├── tools/
│   ├── search_tools.py     # Serper.dev integration
│   ├── browser_tools.py    # Browserless integration
│   └── calculator_tools.py # Budget calculations
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
└── README.md              # This file
```

## Usage Examples

### Streamlit UI
1. Open the Streamlit app
2. Fill in your trip details in the sidebar form
3. Click "Submit" and watch the agents work
4. View your personalized itinerary

### FastAPI
Perfect for integrating into other applications or building custom UIs.

### CLI
Great for automation, scripts, or headless environments.

## Agent Workflow

1. **City Selection Expert** analyzes your preferences and picks the best destination
2. **Local Expert** researches attractions, local customs, and hidden gems
3. **Travel Concierge** creates a detailed itinerary with logistics and budget

Each agent uses specialized tools:
- **Search**: Web research via Serper.dev
- **Browser**: Content extraction via Browserless
- **Calculator**: Cost calculations and budget planning

## Output Format

The system generates:
- **Structured Itinerary**: Day-by-day plans with activities, timing, and logistics
- **Budget Breakdown**: Accommodation, activities, and total cost estimates
- **Local Insights**: Hidden gems and cultural tips

## API Keys Setup

### Gemini API
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add to `.env` as `GEMINI_API_KEY`

### Serper.dev
1. Sign up at [Serper.dev](https://serper.dev)
2. Get your API key from the dashboard
3. Add to `.env` as `SERPER_API_KEY`

### Browserless
1. Sign up at [Browserless.io](https://browserless.io)
2. Get your API key
3. Add to `.env` as `BROWSERLESS_API_KEY`

