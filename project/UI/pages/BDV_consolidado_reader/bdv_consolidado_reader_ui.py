from io import BytesIO
import streamlit as st
from project.UI.pages.page_base_reader import PageBaseReader
from project.readers.excel_reader import ExcelReader
from typing import Optional, Any
import pandas as pd

class BDVConsolidadoReaderUI(PageBaseReader):
    def __init__(self) -> None:
        super().__init__(
            page_name="BDV Consolidado Reader",
            icon="📒",
            description="Page for BDV Consolidado reports analysis."
        )
        self.reader: Optional[ExcelReader] = None
        
    def render(self) -> None:
        st.title(f"{self._icon} {self.page_name}")
        
        if self._description:
            st.markdown(self._description)
            st.divider()
            
        st.number_input("Average Speed Threshold (km/h):", min_value=80, max_value=200, value=100, key='avg_speed_threshold', help="Set the speed threshold to flag over-speeding incidents.")
        
        uploaded_file = st.file_uploader(
            "📁 Upload your file",
            type=self.get_file_types(),
            help=f"Accepted formats: {', '.join(self.get_file_types())}",
            key="bdv_consolidado_file_uploader"
        )
        
        if uploaded_file:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.info(f"📄 **File:** {uploaded_file.name}")
            with col2:
                st.info(f"**Size:** {uploaded_file.size / 1024:.1f} KB")
            
            self._process_file(uploaded_file)
    
    def _process_file(self, uploaded_file: Any) -> None:
        """Process the uploaded BDV Consolidado file.
        
        Args:
            uploaded_file: Streamlit UploadedFile object
        """
        with st.spinner("⏳ Processing BDV Consolidado file..."):
            try:
                self.reader = ExcelReader(file_obj=uploaded_file, header=2, dtype={'Km Rodado': 'float', 'Hora Saída': str, 'Hora Chegada': str, 'Tempo': str})
                self.reader.safe_read()
                
                if self.reader.df is not None:
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
        """Process data specific to BDV Consolidado reports."""
        if self.reader is None or self.reader.df is None:
            st.error("❌ No data loaded. Please upload a file first.")
            return
        
        df = self.reader.df.copy()
        
        columns_to_normalize = ['Hora Saída', 'Hora Chegada', 'Tempo']
        
        for col in columns_to_normalize:
            if col in df.columns:
                df[col] = df[col].astype(str).str.zfill(8)        
        
        df['Velocidade média'] = df.apply(lambda row: ((row['Km Rodado'] * 1000) / self._time_to_seconds(row['Tempo']) * 3.6) if self._time_to_seconds(row['Tempo']) > 0 else 0, axis=1)
        
        threshold = st.session_state.get('avg_speed_threshold', 100)
        df['Status'] = df.apply(lambda row: 'Negative odometer' if row['Km Rodado'] < 0 else ('Over speed' if row['Velocidade média'] > threshold else 'OK'), axis=1)
        
        self.reader.df = df
    
    def _time_to_seconds(self, time_str: str) -> int:
        """Convert time string in HH:MM:SS format to total seconds.
        
        Args:
            time_str: Time string in HH:MM:SS format.
        
        Returns:
            Total seconds as integer.
        """
        try:
            h, m, s = map(int, time_str.split(':'))
            return h * 3600 + m * 60 + s
        except:
            return 0
        
    def display_results(self) -> None:
        """Display results specific to BDV Consolidado reports."""
        if self.reader is None or self.reader.df is None:
            st.error("❌ No data to display. Please upload and process a file first.")
            return
        
        columns_to_show = ['Data', 'Itinerários', 'Hora Saída', 'Hora Chegada', 'Tempo', 'Km Rodado', 'Placa', 'Organização', 'Velocidade média', 'Status']
        
        if self.reader.df['Status'].isin(['Over speed', 'Negative odometer']).any():
            st.warning("⚠️ It seems there are records with issues:")
            df_issues = self.reader.df[self.reader.df['Status'].isin(['Over speed', 'Negative odometer'])][columns_to_show].copy()
            
            df_display = df_issues.copy()
            df_display['Velocidade média'] = df_display['Velocidade média'].round(2).astype(str) + " km/h"
            st.dataframe(df_display.reset_index(drop=True), width='stretch', hide_index=True)
            
            df_issues['Velocidade média'] = df_issues['Velocidade média'].round(2)
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df_display.to_excel(writer, index=False, sheet_name='Issues')
            
            st.download_button(
                label="📥 Download Issues Report",
                data=buffer.getvalue(),
                file_name="bdv_consolidado_issues_report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="bdv_download_issues"
            )
        else:
            st.success("✅ All records are OK.")
        
        
        
            
            