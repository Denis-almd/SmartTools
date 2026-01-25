import streamlit as st
from project.UI.pages.base_page import BasePage


class PageBaseReader(BasePage):
    
    def __init__(self, page_name: str, reader_class, icon: str = "📊", description: str = ""):
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
        return self._description or f"Análise de {self.page_name}"
    
    def render(self):
        st.title(f"{self._icon} {self.page_name}")
        
        if self._description:
            st.markdown(self._description)
            st.divider()
        
        uploaded_file = st.file_uploader(
            "📁 Envie seu arquivo",
            type=self.get_file_types(),
            help=f"Formatos aceitos: {', '.join(self.get_file_types())}"
        )
        
        if uploaded_file:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.info(f"📄 **Arquivo:** {uploaded_file.name}")
            with col2:
                st.info(f"**Tamanho:** {uploaded_file.size / 1024:.1f} KB")
            
            if st.button("🚀 Processar Arquivo", type="primary", use_container_width=True):
                self._process_file(uploaded_file)
    
    def _process_file(self, uploaded_file):
        with st.spinner("⏳ Processando arquivo..."):
            try:
                self.reader = self.reader_class(file_obj=uploaded_file)
                
                result = self.reader.safe_read()
                
                if result and self.reader.df is not None:
                    st.success("✅ Arquivo lido com sucesso!")
                    
                    try:
                        self.process_data()
                    except Exception as e:
                        st.error(f"❌ Erro no processamento: {e}")
                        return
                    
                    self.display_results()
                else:
                    st.error("❌ Erro ao ler o arquivo. Verifique o formato e tente novamente.")
            
            except Exception as e:
                st.error(f"❌ Erro inesperado: {e}")
    
    def get_file_types(self):
        return ['csv', 'xlsx', 'xls']
    
    def process_data(self):
        pass
    
    def display_results(self):
        st.subheader("📋 Dados Carregados")
        st.dataframe(self.reader.df, use_container_width=True)