import streamlit as st
import streamlit as st
from streamlit_mic_recorder import mic_recorder
import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

st.title("GovSense Voice AI")

audio = mic_recorder(
    start_prompt="🎙️ Start recording",
    stop_prompt="⏹️ Stop recording",
    just_once=True
)

if audio:
    st.success("Audio recorded")

    with open("audio.wav", "wb") as f:
        f.write(audio["bytes"])

    with open("audio.wav", "rb") as f:
        transcript = openai.audio.transcriptions.create(
            file=f,
            model="gpt-4o-transcribe"
        )

    st.subheader("Transcript")
    st.write(transcript.text)
