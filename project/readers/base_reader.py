import pandas as pd

class BaseReader:
    
    def __init__(self, file_obj = None, encoding: str = 'utf-8', delimiter: str = ';', header: int = 0, skiprows: int = 0, **kwargs) -> None:
        self.file_obj = file_obj
        self.encoding:str = encoding
        self.delimiter = delimiter
        self.header = header
        self.skiprows = skiprows
        self.reader_config = kwargs
        self.df: pd.DataFrame | None = None
    
    def set_file_obj(self, file_obj):
        self.file_obj = file_obj
        return self
    
    def set_encoding(self, encoding: str):
        self.encoding = encoding
        return self
    
    def set_delimiter(self, delimiter: str):
        self.delimiter = delimiter
        return self
    
    def set_header(self, header: int):
        self.header = header
        return self
    
    def set_config(self, key: str, value):
        self.reader_config[key] = value
        return self
    
    def read(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def safe_read(self):
        try:
            if self.file_obj is None:
                raise ValueError("No file was provided")
            
            return self.read()
        
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            return None
    
    def validate(self) -> bool:
        raise NotImplementedError("Subclasses must implement this method")