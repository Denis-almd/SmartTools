import pandas as pd
from project.readers.base_reader import BaseReader


class ExcelReader(BaseReader):
    
    def __init__(self, file_obj=None, encoding: str = 'utf-8', sheet_name: int | str = 0, **kwargs):
        super().__init__(file_obj, encoding, **kwargs)
        self.sheet_name = sheet_name
    
    def set_sheet_name(self, sheet_name: int | str):
        self.sheet_name = sheet_name
        return self
    
    def read(self):
        try:
            self.df = pd.read_excel(
                self.file_obj,
                sheet_name=self.sheet_name,
                header=self.header,
                skiprows=self.skiprows,
                **self.reader_config
            )
            return self
        except Exception as e:
            raise ValueError(f"Erro ao ler arquivo Excel: {e}")
    
    def validate(self) -> bool:
        if self.df is None:
            return False
        
        if self.df.empty:
            print("⚠️ Aviso: DataFrame está vazio")
            return False
        
        return True
