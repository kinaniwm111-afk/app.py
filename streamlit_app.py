import streamlit as st
import tempfile
import openai
import os

st.title("GovSense Voice AI")
st.write("Upload a voice complaint")

# حطي مفتاح OpenAI هنا (أو في Secrets)
openai.api_key = st.secrets["OPENAI_API_KEY"]

audio_file = st.file_uploader(
    "Upload audio file",
    type=["wav", "mp3", "m4a"]
)

if audio_file is not None:
    st.audio(audio_file)

    if st.button("Analyze Voice Complaint"):
        with st.spinner("Transcribing..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(audio_file.read())
                audio_path = tmp.name

            transcript = openai.Audio.transcribe(
                model="whisper-1",
                file=open(audio_path, "rb")
            )

            text = transcript["text"]

        st.subheader("Transcribed Text")
        st.write(text)

        st.subheader("Analysis")

        anger = "High" if any(w in text.lower() for w in ["angry", "late", "delay", "complaint"]) else "Normal"
        category = "Service Delay" if "delay" in text.lower() else "General"
        priority = "URGENT" if anger == "High" else "Normal"

        st.write(f"Emotion: {anger}")
        st.write(f"Category: {category}")
        st.write(f"Priority: {priority}")

