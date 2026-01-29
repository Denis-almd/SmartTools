import streamlit as st
from typing import Optional
from project.UI.pages.base_page import BasePage
from project.UI.pages.page_manager import PageManager

class SideBar:
    
    def __init__(self) -> None:
        self._render_sidebar()
    
    def _render_sidebar(self) -> None:
        try:
            st.sidebar.title("Navigation")
            st.sidebar.write("Use the sidebar to navigate through different sections of the app.")
            st.sidebar.divider()
            
            page_classes = PageManager.get_page_classes()
            
            options: list[str] = [page_cls().get_name() for page_cls in page_classes]
            
            selection: Optional[str] = st.sidebar.radio("Go to", options)
            
            if selection:
                if 'current_page' not in st.session_state:
                    st.session_state.current_page = selection
                elif st.session_state.current_page != selection:
                    old_page = st.session_state.current_page
                    st.session_state.current_page = selection
                    
                    keys_to_clear = [key for key in st.session_state.keys() 
                                    if key.endswith('_file_uploader') and key != f"{selection.lower().replace(' ', '_')}_file_uploader"]
                    for key in keys_to_clear:
                        if key in st.session_state:
                            del st.session_state[key]
                
                for page_cls in page_classes:
                    temp_instance = page_cls()
                    if temp_instance.get_name() == selection:
                        temp_instance.render()
                        break
        except Exception as e:
            st.sidebar.error(f"Error rendering sidebar: {e}")