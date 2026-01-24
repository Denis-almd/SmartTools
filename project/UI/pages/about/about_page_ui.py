import streamlit as st
from project.UI.pages.base_page import BasePage

class AboutPage(BasePage):
        
    def get_name(self):
        return 'About'
    
    def get_icon(self):
        return 'ℹ️'
    
    def get_description(self):
        return 'Learn more about the Smart Tools application.'
    
    def render(self):
        st.title("About Smart Tools ℹ️")
        st.write("""
        Smart Tools is an application designed to enhance productivity by providing a suite of intelligent tools. 
        
        The idea behind Smart Tools is to integrate various functionalities into a single platform, making it easier for users to access and utilize these tools efficiently.
        
        **Features:**
        - User-friendly interface
        - Variety of productivity tools
        - Easy navigation through sidebar
        - Modular design for easy expansion
        
        **Developed by: Denis Almeida** - denis.almeida@meta.com.br
        
        Free feel to reach out for any questions, improvements or feedback!
        """)