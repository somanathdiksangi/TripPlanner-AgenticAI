# 🌍 TripPlanner-AgenticAI

An intelligent travel planning application powered by **CrewAI** agents and a **Streamlit** frontend. This tool helps users plan personalized trips based on preferences like dates, origin, interests, and destinations — with real-time insights on weather, events, and travel costs.

## ✈️ Overview

TripPlanner-AgenticAI leverages agentic AI architecture to coordinate multiple AI agents with distinct roles, such as:

- **City Selection Expert**: Analyzes travel destinations based on weather, events, and cost.
- **Flight Finder Agent**: Fetches real-time flight costs and options.
- **Attractions Guide Agent**: Curates attractions based on user interests like swimming, hiking, and food.
- **Itinerary Generator**: Builds a day-by-day itinerary tailored to the user.

## 🎯 Features

- 🧠 **Autonomous multi-agent decision making** (via CrewAI)
- 📅 Smart city and itinerary selection based on:
  - Weather conditions
  - Seasonal events
  - Travel cost estimates
- 🌐 Real-time output via a **Streamlit dashboard**
- 🔗 Easily extendable with additional agents or APIs

## 🧱 Tech Stack

| Component      | Technology              |
|----------------|-------------------------|
| Backend        | Python, CrewAI, LiteLLM |
| Frontend       | Streamlit               |
| Agent Routing  | CrewAI Task-Flow        |
| LLM Support    | Gemini                  |
| Environment    | Conda / venv            |

