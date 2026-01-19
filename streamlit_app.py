import streamlit as st
import tempfile
import whisper

st.title("GovSense Voice AI")
st.write("Upload a complaint voice recording")

# تحميل موديل Whisper
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# رفع الصوت
audio_file = st.file_uploader(
    "Upload audio file",
    type=["wav", "mp3", "m4a"]
)

if audio_file is not None:
    st.audio(audio_file)

    if st.button("Analyze Voice Complaint"):
        with st.spinner("Transcribing audio..."):
            # حفظ الصوت مؤقتًا
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(audio_file.read())
                audio_path = tmp.name

            # تحويل الصوت إلى نص
            result = model.transcribe(audio_path, language="en")
            text = result["text"]

        st.subheader("Transcribed Text")
        st.write(text)

        # تحليل بسيط (مبدئي)
        st.subheader("Analysis Result")

        anger = "High" if any(word in text.lower() for word in ["angry", "late", "complaint", "delay"]) else "Normal"
        category = "Service Delay" if "delay" in text.lower() else "General"
        priority = "URGENT" if anger == "High" else "Normal"

        st.write(f"Emotion: {anger}")
        st.write(f"Category: {category}")
        st.write(f"Priority: {priority}")
