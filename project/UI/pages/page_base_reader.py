import streamlit as st
from project.UI.pages.base_page import BasePage
from project.readers.excel_reader import ExcelReader


class PageBaseReader(BasePage):    
    def __init__(self, page_name: str, reader_class = ExcelReader, icon: str = "📊", description: str = ""):
        self.page_name = page_name
        self.reader_class = reader_class
        self.reader = None
        self._icon = icon
        self._description = description
    
    def get_name(self) -> str:
        return self.page_name
    
    def get_icon(self) -> str:
        return self._icon
    
    def get_description(self) -> str:
        return self._description or f"Analysis of {self.page_name}"
    
    def render(self) -> None:
        st.title(f"{self._icon} {self.page_name}")
        
        if self._description:
            st.markdown(self._description)
            st.divider()
        
        uploaded_file = st.file_uploader(
            "📁 Upload your file",
            type=self.get_file_types(),
            help=f"Accepted formats: {', '.join(self.get_file_types())}"
        )
        
        if uploaded_file:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.info(f"📄 **File:** {uploaded_file.name}")
            with col2:
                st.info(f"**Size:** {uploaded_file.size / 1024:.1f} KB")
            
            self._process_file(uploaded_file)
    
    
    def _process_file(self, uploaded_file):
        with st.spinner("⏳ Processing file..."):
            try:
                self.reader = self.reader_class(file_obj=uploaded_file)
                
                result = self.reader.safe_read()
                
                if result and self.reader.df is not None:
                    st.success("✅ File read successfully!")
                    
                    try:
                        self.process_data()
                    except Exception as e:
                        st.error(f"❌ Processing error: {e}")
                        return
                    
                    self.display_results()
                else:
                    st.error("❌ Error reading file. Please check the format and try again.")
            
            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")
    
    def get_file_types(self):
        return ["xlsx", "xls"]
    
    def process_data(self):
        pass
    
    def display_results(self):
        st.subheader("📋 Loaded Data")
        st.dataframe(self.reader.df, use_container_width=True)