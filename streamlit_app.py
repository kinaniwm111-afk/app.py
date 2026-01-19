import streamlit as st

st.title("GovSense Voice AI")
st.write("Demo: Voice-based complaint analysis")

st.metric("Complaints Today", 12)
st.metric("Urgent Complaints", 5)

anger = st.slider("Anger Level", 0, 100, 85)

if st.button("Analyze Complaint"):
    st.subheader("Result")
    st.write("Emotion: High Anger")
    st.write("Category: Service Delay")
    st.write("Priority: URGENT")
