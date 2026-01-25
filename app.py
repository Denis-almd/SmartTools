import streamlit as st
from project.UI.side_bar import SideBar

APP_CONFIG = {
    "page_title": "Smart Tools",
    "page_icon": "🏠",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

def configure_page():
    """Configura a página do Streamlit"""
    st.set_page_config(**APP_CONFIG)

def run_app():
    configure_page()
    SideBar()

if __name__ == "__main__":
    run_app()