import streamlit as st
from project.UI import side_bar


APP_CONFIG = {
    "page_title": "Smart Tools",
    "page_icon": "🏠",
    "layout": "wide",  # Considere "centered" para melhor UX
    "initial_sidebar_state": "expanded"
}

def configure_page():
    """Configura a página do Streamlit"""
    st.set_page_config(**APP_CONFIG)
def run_app():
    configure_page()
    side_bar.SideBar()

if __name__ == "__main__":
    run_app()