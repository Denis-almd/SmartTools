import streamlit as st

class TimeConverter:      

    def create_ui(self):
        st.header("Convert HH:MM:SS to Seconds and Vice Versa ⏰")
        st.write("Enter time in HH:MM:SS format or seconds to convert:")
        st.time_input("Time Input (HH:MM:SS)", key="time_input")