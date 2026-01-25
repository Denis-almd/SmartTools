import streamlit as st
from typing import Optional
from project.UI.pages.base_page import BasePage
from project.UI.pages.page_manager import PageManager

class SideBar:
    
    def __init__(self) -> None:
        self.pages: list[BasePage] = PageManager.get_pages()
        self._render_sidebar()
    
    def _render_sidebar(self) -> None:
        try:
            st.sidebar.title("Navigation")
            st.sidebar.write("Use the sidebar to navigate through different sections of the app.")
            st.sidebar.divider()
            
            options: list[str] = [page.get_name() for page in self.pages]
            
            selection: Optional[str] = st.sidebar.radio("Go to", options)
            
            if selection:
                for page in self.pages:
                    if page.get_name() == selection:
                        page.render()
                        break
            
        except Exception as e:
            st.sidebar.error(f"Error rendering sidebar: {e}")