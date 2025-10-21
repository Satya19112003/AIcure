import streamlit as st
from diagnosis import process_inputs
from PIL import Image
import tempfile

st.title("🩺 AIcura - Your AI Health Assistant")

symptoms = st.text_input("Describe Your Symptoms", placeholder="e.g., I have a rash on my arm")

uploaded_file = st.file_uploader("Upload Image (Optional)", type=["png", "jpg", "jpeg"])

image_path = None
if uploaded_file is not None:
    # Save uploaded image to a temp file because process_inputs expects filepath
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        image_path = tmp_file.name

if st.button("Get Diagnosis"):
    text_response, audio_response_path = process_inputs(symptoms, image_path)
    
    st.text_area("Doctor's Response", value=text_response, height=150)
    
    if audio_response_path and not audio_response_path.startswith("Text-to-Speech Error"):
        audio_file = open(audio_response_path, "rb")
        st.audio(audio_file.read(), format='audio/mp3')

