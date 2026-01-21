import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from project.utils.emojis import Emojis
from project.UI.side_bar import SideBar


class MainPage:    
    def __init__(self):
        self.sidebar = SideBar()
    
    def run(self):
        self._display_content()    
    
    def _display_content(self):
        try:
            self.sidebar.render_sidebar()
        except Exception as e:
            st.error(f"Error rendering sidebar: {e}")