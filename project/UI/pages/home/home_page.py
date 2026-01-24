import streamlit as st
from project.tools.tool_manager import ToolRegister
from project.UI.pages.base_page import BasePage

class HomePage(BasePage):
    
    def __init__(self):
        self.tools = ToolRegister.get_tools()
        
    def get_name(self):
        return 'Home'
    
    def render(self):
        try:
            st.title("Welcome to Smart Tools Home Page 🏠")
            st.write("Below you will find Smart tools to enhance your productivity.")
            #st.divider()
            
            self._tabs()
        except Exception as e:
            st.error(f"Error displaying content: {e}")
            
    def _tabs(self):
        
        if not self.tools:
            st.info("No tools available.")
            return
        
        tab_labels = [f"{tool.get_icon()} {tool.get_name()}" for tool in self.tools]
        tabs = st.tabs(tab_labels)
        
        for tab, tool in zip(tabs, self.tools):
            with tab:
                try:
                    tool.render()
                except Exception as e:
                    st.error(f"Error loading tool '{tool.get_name()}': {e}")
                