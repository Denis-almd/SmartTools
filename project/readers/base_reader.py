import pandas as pd

class BaseReader:
    
    def __init__(self, file_obj = None, encoding: str = 'utf-8', header: int = 0, skiprows: int = 0, dtype: dict | type = str, **kwargs) -> None:
        self.file_obj = file_obj
        self.encoding:str = encoding
        self.header: int = header
        self.skiprows: int = skiprows
        self.dtype: dict | type = dtype
        self.reader_config: dict = kwargs
        self.df: pd.DataFrame | None = None
    
    def set_file_obj(self, file_obj) -> 'BaseReader':
        self.file_obj = file_obj
        return self
    
    def set_encoding(self, encoding: str) -> 'BaseReader':
        self.encoding = encoding
        return self
    
    def set_header(self, header: int) -> 'BaseReader':
        self.header = header
        return self
    
    def set_config(self, key: str, value) -> 'BaseReader':
        self.reader_config[key] = value
        return self
    
    def read(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")
    
    def safe_read(self) -> bool:
        try:
            if self.file_obj is None:
                raise ValueError("No file was provided")
            
            self.read()
            return True
        
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            return False
    
    def validate(self) -> bool:
        raise NotImplementedError("Subclasses must implement this method")