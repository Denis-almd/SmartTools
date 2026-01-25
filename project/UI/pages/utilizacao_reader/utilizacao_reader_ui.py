import streamlit as st
from project.UI.pages.reader_base_page import PageBaseReader
from project.readers.excel_reader import ExcelReader

class UtilizacaoReader(PageBaseReader):
    """
    Página para análise do relatório de utilização de.
    
    Exemplo de uso da arquitetura de leitores.
    Aceita arquivos Excel com colunas: LeitorID, DataHora, Evento
    """
    
    def __init__(self):
        super().__init__(
            page_name="Relatório de Utilização de Leitores",
            reader_class=ExcelReader,
            icon="📚",
            description="📈 Analise os dados de utilização dos leitores de forma eficiente."
        )
    
    def get_file_types(self):
        """Aceita apenas arquivos Excel."""
        return ['xlsx', 'xls']
    
    def process_data(self):
        """
        Processa os dados específicos do relatório de utilização de leitores.
        Adiciona colunas calculadas e converte tipos.
        """
        df = self.reader.df
        
        # Converte nomes de colunas para minúsculas e remove espaços
        df.columns = df.columns.str.lower().str.strip()
        
        # Verifica se as colunas necessárias existem
        required_columns = ['leitorid', 'datahora']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            st.warning(f"⚠️ Colunas não encontradas: {', '.join(missing_columns)}")
        else:
            # Converte coluna de datahora
            try:
                df['datahora'] = pd.to_datetime(df['datahora'])
            except:
                st.warning("⚠️ Não foi possível converter a coluna 'DataHora'")
        
        # Atualiza o DataFrame no reader
        self.reader.df = df
    
    def display_results(self):
        """Exibição customizada para relatório de utilização de leitores."""
        df = self.reader.df



