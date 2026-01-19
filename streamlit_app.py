import streamlit as st

st.title("GovSense Voice AI")

st.write("Demo: Voice-based complaint analysis")

if st.button("Analyze Complaint"):
    st.write("Emotion: High Anger")
    st.write("Category: Service Delay")
    st.write("Priority: URGENT")
