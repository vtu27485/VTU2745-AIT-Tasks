
Title

StudyMate AI – AI-Powered College Study Assistant Using Google Gemini

Aim

To develop a simple AI-powered study assistant using Python and Google Gemini API that helps college students interact with an AI chatbot through text and voice, and obtain answers from uploaded PDF study materials.

Algorithm
Start the application.
Initialize the Streamlit interface and configure the StudyMate AI application.
Load the Gemini API key and establish a connection with the Google Gemini model.
Display the StudyMate AI interface with text chat, voice input, and PDF upload options.
Accept the student's input through:
Text question
Voice question
Uploaded PDF study material
If a PDF is uploaded, use PyPDF to extract the text from the document.
Prepare the user's question and relevant PDF content as input for Gemini.
Send the input to the Gemini AI model using the Google GenAI Python SDK.
Generate an AI-based response according to the student's question.
Display the generated response in the Streamlit chatbot interface.
Store the conversation so previous messages remain visible during the session.
Allow the user to clear the conversation and start a new session.
Stop the application when the user closes it.
Simple Flow
START
  ↓
Initialize StudyMate AI
  ↓
Connect to Google Gemini API
  ↓
User enters Text / Voice / PDF
  ↓
Process User Input
  ↓
Extract PDF Text if PDF is uploaded
  ↓
Send Input to Gemini
  ↓
Generate AI Response
  ↓
Display Response
  ↓
Continue Chat?
  ├── YES → Take Next Question
  └── NO  → END
Technologies Used
Python
Streamlit
Google Gemini API
Google GenAI Python SDK
PyPDF

This title and algorithm accurately match the application you've built.

import streamlit as st
from google import genai

st.set_page_config(page_title="StudyMate AI", page_icon="🤖")

st.title("🤖 StudyMate AI")
st.write("Your personal AI study assistant")

api_key = st.text_input("Enter Gemini API Key", type="password")

question = st.text_area(
    "Ask your question:",
    placeholder="Example: Explain Python loops in simple words"
)

if st.button("Ask AI"):
    if not api_key:
        st.error("Please enter your Gemini API key.")
    elif not question:
        st.warning("Please enter a question.")
    else:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=f"""
            You are StudyMate, a helpful college study assistant.

            Explain concepts in simple language.
            Give examples when useful.
            Keep answers suitable for students.

            Student question:
            {question}
            """
        )

        st.subheader("🤖 StudyMate")
        st.write(response.text)

