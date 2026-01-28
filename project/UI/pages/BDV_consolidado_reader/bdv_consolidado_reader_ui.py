import streamlit as st
from project.UI.pages.page_base_reader import PageBaseReader
from project.readers.excel_reader import ExcelReader
from typing import Optional, Any
import pandas as pd

class BDVConsolidadoReaderUI(PageBaseReader):
    def __init__(self) -> None:
        super().__init__(
            page_name="BDV Consolidado Reader",
            icon="",
            description="Page for BDV Consolidado reports analysis."
        )
        self.reader: Optional[ExcelReader] = None
    
    def _process_file(self, uploaded_file: Any) -> None:
        """Process the uploaded BDV Consolidado file.
        
        Args:
            uploaded_file: Streamlit UploadedFile object
        """
        with st.spinner("⏳ Processing BDV Consolidado file..."):
            try:
                self.reader = ExcelReader(file_obj=uploaded_file)
                
                result = self.reader.safe_read()
                
                if result and self.reader.df is not None:
                    st.success(f"✅ {self.reader.file_obj.name} file read successfully!")
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
    
    def process_data(self) -> None:
        st.success("Processing data...")