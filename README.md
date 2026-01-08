✈️ Agentic AI Travel Planner

A multi-agent AI travel planning system that autonomously researches destinations, finds accommodations, recommends local food, plans transportation, and generates a complete day-by-day itinerary based on user preferences and budget.

This project demonstrates agentic AI design, LLM orchestration, and real-time tool usage in a practical, real-world application.

🚀 Features

🧠 Multi-Agent Architecture – Each agent handles a specific responsibility

🌍 Live Web Search – Real-time data using DuckDuckGo tools

💰 Budget-Aware Planning – Tailored recommendations based on user budget

📅 End-to-End Itinerary Generation – Morning, afternoon, and evening plans

🧩 Modular & Extensible – Easily add new agents or tools

🖥️ Streamlit UI – Interactive web interface for users

🤖 Agent Workflow

Destination Research Agent
Finds top attractions and must-see places

<img width="1898" height="1132" alt="image" src="https://github.com/user-attachments/assets/8663521b-e795-414a-a3a3-bf897a4d0db0" />


Accommodation Agent
Identifies budget-friendly hotels and stays

Food & Dining Agent
Recommends local dishes and popular restaurants

Transportation Agent
Plans public transport and local travel options

Itinerary Planner Agent
Synthesizes all agent outputs into a structured itinerary

🛠️ Tech Stack

Python

Agno (Agent framework)

Groq LLM API (LLaMA 3.1)

DuckDuckGo Tools (Web search)

Streamlit (UI)

dotenv (Environment management)

📂 Project Structure
Travelagent/
│
├── app.py               # Streamlit application
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .env                 # API keys (local only, not committed)

▶️ Run the Application
streamlit run app.py


Open in browser:

http://localhost:8501

🌐 Deployment (Hugging Face Spaces)

Push code to Hugging Face Space

Add GROQ_API_KEY in Settings → Secrets

Ensure requirements.txt includes:

agno
groq
streamlit
python-dotenv

📸 Demo

https://github.com/user-attachments/assets/9b9c0b86-7bfd-47d5-bf6f-8e2320409c1b


🎯 Use Cases

Personalized travel planning

AI-powered itinerary generation

Demonstration of agentic AI systems

GenAI / ML engineering portfolio project

🔮 Future Enhancements

Chat-based travel planning interface

PDF itinerary export

Cost breakdown per day

Hotel and flight booking integrations

Persistent memory per user

👩‍💻 Author

Varshini Kanumuri
AI / ML / GenAI Enthusiast

📌 Open to opportunities in AI, ML, and GenAI engineering

📄 License

This project is licensed under the MIT License.
