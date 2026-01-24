import streamlit as st
from project.UI.pages.base_page import BasePage

class UtilizacaoReader(BasePage):
    def get_name(self) -> str:
        return "Utilização Reader"
    
    def get_icon(self) -> str:
        return "📖"
    
    def get_description(self) -> str:
        return "Read and analyze utilização data from ."

    def render(self):
        st.header("Welcome to Utilização report Reader 📖")
        st.write("This tool allows you to read and analyze utilização report data.")
        # Additional UI components and logic for the Utilização Reader can be added here.
        self._file_upload()
        
        
    def _file_upload(self):
        try:
            uploaded_file = st.file_uploader("Upload your utilização report data file", type=["csv", "xlsx", "txt"])
        except Exception as e:
            st.error(f"Error uploading file: {e}")            
            
        if uploaded_file:        
            with st.spinner("loading file... Please wait."):                
               data = self._load_file(uploaded_file)
            
            if data is not None:
                st.success("File loaded successfully!")
                st.dataframe(data.head())
            else:
                st.error("Failed to load the file. Please check the file format and try again.")
    
    @st.cache_data            
    def _load_file(self, file):
        try:
            import pandas as pd
            if file.name.endswith('.csv'):
                return pd.read_csv(file)
            elif file.name.endswith('.xlsx'):
                return pd.read_excel(file)
            elif file.name.endswith('.txt'):
                return pd.read_csv(file, delimiter='\t')
            else:
                st.error("Unsupported file format.")
                return None
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return None