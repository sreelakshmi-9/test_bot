import streamlit as st
from datetime import datetime
import random

def generate_appointment_id():
    return f"APT-{random.randint(1000, 9999)}"

st.set_page_config(page_title="Medical AI Assistant", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Book Appointment", "Symptom Checker", "Medical Q&A"])

if page == "Home":
    st.title("Welcome to Medical AI Assistant")
    st.write("Use this AI-powered system for real-time medical assistance.")
    st.image("https://source.unsplash.com/800x400/?healthcare,doctor")

elif page == "Book Appointment":
    st.title("Book an Appointment")
    with st.form("appointment_form"):
        name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        doctor = st.selectbox("Select Doctor", ["Dr. Smith (Cardiologist)", "Dr. Johnson (Dermatologist)", "Dr. Lee (Pediatrician)"])
        date = st.date_input("Select Date", min_value=datetime.today())
        time = st.time_input("Select Time")
        submit = st.form_submit_button("Book Appointment")
    
    if submit:
        appointment_id = generate_appointment_id()
        st.success(f"Appointment confirmed! ID: {appointment_id}")

elif page == "Symptom Checker":
    st.title("AI-Powered Symptom Checker")
    symptoms = st.text_area("Enter your symptoms (comma-separated)")
    if st.button("Check Symptoms"):
        st.write("Analyzing symptoms...")
        st.success("You may have a common cold or flu. Please consult a doctor for further advice.")

elif page == "Medical Q&A":
    st.title("Medical Q&A")
    question = st.text_area("Ask a medical question")
    if st.button("Get Answer"):
        st.write("Processing your question...")
        st.success("AI Response: Based on medical data, here is the best advice... (Placeholder response)")

st.sidebar.info("Developed using Streamlit and Agentic AI.")
