from project.UI.pages.page_base_reader import PageBaseReader
import streamlit as st
import pandas as pd
from io import BytesIO
from project.readers.excel_reader import ExcelReader
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

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
                    st.success(f"✅ {self.reader.file_obj.name} file read successfully!")
                    try:
                        self.process_data()
                    except Exception as e:
                        st.error(f"❌ Processing error: {e}")
            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")
    
    
    def process_data(self):
        df = self.reader.df
        
        #df = df.dropna(subset=['Km Inicial', 'Km Final'], how='any')
        
        if 'Km Inicial' in df.columns:
            df['Km Inicial'] = pd.to_numeric(df['Km Inicial'], errors='coerce')
        
        if 'Km Final' in df.columns:
            df['Km Final'] = pd.to_numeric(df['Km Final'], errors='coerce')
        
        #df = df.sort_values(['Veículo', 'Data']).reset_index(drop=True)
        
        inconsistencias = []
        
        for veiculo in df['Veículo'].unique():
            df_veiculo = df[df['Veículo'] == veiculo]
            
            for i in range(1, len(df_veiculo)):
                km_final_anterior = df_veiculo.iloc[i-1]['Km Final']
                km_inicial_atual = df_veiculo.iloc[i]['Km Inicial']
                    
                if pd.notna(km_final_anterior) and pd.notna(km_inicial_atual):
                    if km_final_anterior != km_inicial_atual:
                        inconsistencias.append({
                            'Veículo': veiculo,
                            'Data Anterior': df_veiculo.iloc[i-1]['Data'],
                            'Km Final Anterior': km_final_anterior,
                            'Data Atual': df_veiculo.iloc[i]['Data'],
                            'Km Inicial Atual': km_inicial_atual,
                            'Diferença': km_inicial_atual - km_final_anterior
                        })
        
        self.reader.df = df
        self.df_inconsistencias = pd.DataFrame(inconsistencias) if inconsistencias else None
        self.display_results()
    
    def display_results(self):
        if self.df_inconsistencias is not None and len(self.df_inconsistencias) > 0:
            st.subheader("⚠️ KM Inconsistencies")
            st.warning(f"Found {len(self.df_inconsistencias)} inconsistencies where KM Final ≠ KM Inicial")
            st.dataframe(self.df_inconsistencias, width='stretch', hide_index=True)
            
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                self.df_inconsistencias.to_excel(writer, index=False, sheet_name='Inconsistencies')
            buffer.seek(0)
            
            st.download_button(
                label="📥 Download Inconsistencies (Excel)",
                data=buffer,
                file_name="km_inconsistencies.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.success("✅ No KM inconsistencies found! All odometer readings are continuous.")