import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from project.UI.pages import page_manager

class SideBar:
    
    def __init__(self):
        self.pages = page_manager.PageManager.get_pages()
        self._render_sidebar()
    
    def _render_sidebar(self):
        try:
            st.sidebar.title("Navigation")
            st.sidebar.write("Use the sidebar to navigate through different sections of the app.")
            st.sidebar.divider()
            
            options = [page.get_name() for page in self.pages]
            
            selection = st.sidebar.radio("Go to", options)
            
            if selection:
                for page in self.pages:
                    if page.get_name() == selection:
                        page.render()
                        break
            
        except Exception as e:
            st.sidebar.error(f"Error rendering sidebar: {e}")