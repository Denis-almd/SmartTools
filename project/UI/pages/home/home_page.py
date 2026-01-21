import streamlit as st

class HomePage:
    
    def __init__(self):
        pass
    
    def run(self):
        self._app_config()
        self._display_content()
    
    def _app_config(self):
        try:
            st.set_page_config(
                page_title="Home Page",
                page_icon="🏠",
                layout="wide",
                initial_sidebar_state="expanded"
            )
        except Exception as e:
            st.error(f"Error setting page config: {e}")
    
    def _display_content(self):
        try:
            st.title("Welcome to Smart Tools Home Page 🏠")
            st.write("Below you will find Smart tools to enhance your productivity.")
            st.divider()
            
            self.tabs()
            
            
        except Exception as e:
            st.error(f"Error displaying content: {e}")
            
    def tabs(self):
        try:
            time_converter_tab, json_formatter_tab = st.tabs(["Time Converter ⏰", "JSON Formatter 📄"])
            
            with time_converter_tab:
                st.header("Time Converter ⏰")
                st.write("Convert time between different formats and time zones.")
                
            with json_formatter_tab:
                st.header("JSON Formatter 📄")
                st.write("Format and validate your JSON data easily.")
                
        except Exception as e:
            st.error(f"Error creating tabs: {e}")