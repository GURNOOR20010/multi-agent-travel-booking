# ✈️ LangGraph Multi-Agent Travel Booking System

An AI-powered **multi-agent travel planning system** built using **LangGraph, Groq, Tavily, AviationStack, and PostgreSQL**.

The system takes a user's travel request and uses multiple specialized AI agents to search for flights, research hotels, create a personalized itinerary, and generate a final travel response.

## 🚀 Features

- ✈️ Flight Agent — searches flight information
- 🏨 Hotel Agent — researches hotels and accommodation
- 🗺️ Itinerary Agent — generates a complete travel itinerary
- 🤖 Final Response Agent — combines all results into one response
- 🧠 PostgreSQL-based persistent memory
- 🔎 Web research using Tavily
- ⚡ Groq LLM integration
- 💻 Streamlit frontend
- 🐍 Python-based backend
- 🔗 LangGraph multi-agent workflow

## 🏗️ Architecture

```text
                    USER
                     │
                     ▼
             ┌───────────────┐
             │  Flight Agent │
             │ AviationStack │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │  Hotel Agent  │
             │    Tavily     │
             └───────┬───────┘
                     │
                     ▼
             ┌─────────────────┐
             │ Itinerary Agent │
             │    Groq LLM     │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  Final Agent    │
             │    Groq LLM     │
             └────────┬────────┘
                      │
                      ▼
              FINAL TRAVEL PLAN
                      │
                      ▼
             ┌─────────────────┐
             │   PostgreSQL    │
             │   Checkpointer  │
             └─────────────────┘


langgraph-multi-agent-travel-booking/
│
├── main.py
├── frontend.py
├── requirements.txt
├── .env
├── .gitignore
│
└── tools/
    ├── flight_tool.py
    └── tavily_tool.py


## 🛠️ Tech Stack

- Python
- LangGraph
- LangChain
- Groq
- Tavily
- AviationStack
- PostgreSQL
- Psycopg
- Streamlit
- python-dotenv
- REST APIs
