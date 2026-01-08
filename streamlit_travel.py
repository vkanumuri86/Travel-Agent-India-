import os
import time
from dotenv import load_dotenv

import streamlit as st
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

# Load .env and set key
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

MODEL = "llama-3.1-8b-instant"

st.set_page_config(page_title="Agentic Travel Planner", page_icon="✈️")

st.title("✈️ Agentic Travel Planner")
st.write("Plan a trip using multiple agents for research, hotels, food, transport, and itinerary.")

# Sidebar / inputs
with st.sidebar:
    st.header("Trip Details")
    destination = st.text_input("Destination", value="Hyderabad, India")
    duration = st.number_input("Duration (days)", min_value=1, value=5, step=1)
    budget = st.number_input("Total Budget (₹)", min_value=1000, value=20000, step=1000)
    run_btn = st.button("Plan Trip")

# Helper to create agents
def create_destination_agent():
    return Agent(
        name="Destination Research Agent",
        model=Groq(id=MODEL),
        tools=[DuckDuckGoTools()],
        instructions=[
            "Find top attractions and must-see places",
            "Report ACTUAL search results",
            "List top 3-5 attractions only",
            "Do NOT mention knowledge cutoff",
        ],
        markdown=True,
    )

def create_hotel_agent():
    return Agent(
        name="Accommodation Agent",
        model=Groq(id=MODEL),
        tools=[DuckDuckGoTools()],
        instructions=[
            "Find hotel and accommodation options",
            "Report ACTUAL search results",
            "Focus on mid-range options",
            "Include approximate prices if available",
        ],
        markdown=True,
    )

def create_food_agent():
    return Agent(
        name="Food & Dining Agent",
        model=Groq(id=MODEL),
        tools=[DuckDuckGoTools()],
        instructions=[
            "Find popular local restaurants and food",
            "Report ACTUAL search results",
            "List top 3 must-try dishes or restaurants",
        ],
        markdown=True,
    )

def create_transport_agent():
    return Agent(
        name="Transportation Agent",
        model=Groq(id=MODEL),
        tools=[DuckDuckGoTools()],
        instructions=[
            "Find transportation options within the city",
            "Report ACTUAL search results",
            "Include public transport and taxi info",
        ],
        markdown=True,
    )

def create_planner_agent():
    return Agent(
        name="Itinerary Planner",
        model=Groq(id=MODEL),
        tools=[],
        instructions=[
            "Create a day-by-day itinerary",
            "Based on information provided above",
            "Keep it realistic and budget-friendly",
            "Include morning, afternoon, evening activities",
        ],
        markdown=True,
    )

if run_btn:
    if not destination:
        st.error("Please enter a destination.")
        st.stop()

    st.subheader(f"Trip to {destination}")
    st.write(f"**Duration:** {duration} days | **Budget:** ₹{int(budget)}")

    # Step 1: Destination research
    with st.expander("🌍 Step 1: Destination research", expanded=True):
        dest_placeholder = st.empty()
        dest_placeholder.info("Researching top attractions...")
        dest_agent = create_destination_agent()
        dest_response = dest_agent.run(
            f"What are the top tourist attractions in {destination}?"
        )
        dest_placeholder.markdown(dest_response.content)

    # Small pause (optional)
    time.sleep(1)

    # Step 2: Accommodation
    with st.expander("🏨 Step 2: Accommodation options", expanded=True):
        hotel_placeholder = st.empty()
        hotel_placeholder.info("Finding mid-range hotel options...")
        hotel_agent = create_hotel_agent()
        per_night = int(budget // duration)
        hotel_response = hotel_agent.run(
            f"Find good hotels in {destination} for ${per_night} per night budget"
        )
        hotel_placeholder.markdown(hotel_response.content)

    time.sleep(1)

    # Step 3: Food & dining
    with st.expander("🍽️ Step 3: Local food & dining", expanded=True):
        food_placeholder = st.empty()
        food_placeholder.info("Finding popular local foods and restaurants...")
        food_agent = create_food_agent()
        food_response = food_agent.run(
            f"What are the best local foods and restaurants in {destination}?"
        )
        food_placeholder.markdown(food_response.content)

    time.sleep(1)

    # Step 4: Transportation
    with st.expander("🚗 Step 4: Transportation & logistics", expanded=True):
        transport_placeholder = st.empty()
        transport_placeholder.info("Checking transportation options in the city...")
        transport_agent = create_transport_agent()
        transport_response = transport_agent.run(
            f"What are the best ways to get around {destination}? Public transport options?"
        )
        transport_placeholder.markdown(transport_response.content)

    time.sleep(1)

    # Step 5: Final itinerary
    with st.expander("📋 Step 5: Final itinerary", expanded=True):
        planner_placeholder = st.empty()
        planner_placeholder.info("Creating day-by-day itinerary...")
        planner_agent = create_planner_agent()
        planner_response = planner_agent.run(
            f"Based on the information above, create a {duration}-day itinerary for {destination} "
            f"with budget of ₹{int(budget)}. Include daily activities, meals, and estimated costs."
        )
        planner_placeholder.markdown(planner_response.content)

    st.success("Trip planning complete! You can expand the sections above to review each step.")

