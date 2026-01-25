from project.UI.pages.page_base_reader import PageBaseReader
import streamlit as st
from project.readers.excel_reader import ExcelReader

class UtilizacaoReader(PageBaseReader):
    def __init__(self):
        super().__init__(
            page_name="Utilização Reader",
            icon="📚",
            description="Page for Utilização reports analysis."
        )
    
    def _process_file(self, uploaded_file):
        with st.spinner("⏳ Processing Utilização file..."):
            try:
                self.reader = ExcelReader(file_obj=uploaded_file, header=3)
                
                result = self.reader.safe_read()
                
                if result and self.reader.df is not None:
                    st.success("✅ Utilização file read successfully!")
                    self.display_results()
                    try:
                        self.process_data()
                    except Exception as e:
                        st.error(f"❌ Processing error: {e}")
            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")
        
    def display_results(self):
        st.header("Utilização Data Overview")
        st.dataframe(self.reader.df.head(10))