import pandas as pd
from project.readers.base_reader import BaseReader


class CSVReader(BaseReader):
    
    def __init__(self, file_obj=None, encoding: str = 'utf-8', delimiter: str = ';', **kwargs):
        super().__init__(file_obj, encoding, delimiter, **kwargs)
    
    def read(self):
        try:
            self.df = pd.read_csv(
                self.file_obj,
                encoding=self.encoding,
                delimiter=self.delimiter,
                header=self.header,
                skiprows=self.skiprows,
                **self.reader_config
            )
            return self
        except Exception as e:
            raise ValueError(f"Erro ao ler arquivo CSV: {e}")
    
    def validate(self) -> bool:
        if self.df is None:
            return False
        
        if self.df.empty:
            print("⚠️ Aviso: DataFrame está vazio")
            return False
        
        return True
