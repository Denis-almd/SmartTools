import streamlit as st

from project.utils.emojis import Emojis

class MainPage:
    
    def __init__(self):
        pass
    
    def run(self):
        self._app_config()
        self._display_content()
    
    def _app_config(self):
        try:
            st.set_page_config(
                page_title="Smart Tools",
                page_icon=f'{Emojis.LINK}',
                layout="wide",
                initial_sidebar_state="expanded"
            )
        except Exception as e:
            st.error(f"Error setting page config: {e}")
    
    def _display_content(self):
        try:
            st.title(f"Welcome to Smart Tools {Emojis.HOME}")
            st.write("This is the main page of the Smart Tools application.")
            st.divider()
            
            tab1 = st.tabs([f'BDV Consolidado Reader {Emojis.BOOK}'])
            
            with tab1[0]:
                st.header("BDV Consolidado Reader")
                st.write("Functionality to read and process BDV Consolidado files.")
            
        except Exception as e:
            st.error(f"Error displaying content: {e}")