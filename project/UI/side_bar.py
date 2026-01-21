import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from project.UI.pages.home.home_page import HomePage

class SideBar:
    
    def __init__(self):
        self.home_page = HomePage()
        self.render_sidebar()
    
    def render_sidebar(self):
        try:
            st.sidebar.title("Navigation")
            st.sidebar.write("Use the sidebar to navigate through different sections of the app.")
            st.sidebar.divider()
            
            selection = st.sidebar.radio("Go to", ["Home", "BDV Consolidado Reader", "About"])
            
            match selection:
                case "Home":
                    self.home_page.render_home_page()
            
        except Exception as e:
            st.sidebar.error(f"Error rendering sidebar: {e}")