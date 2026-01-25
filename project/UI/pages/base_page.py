from abc import ABC, abstractmethod

class BasePage(ABC):
    
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        pass
    
    def get_icon(self) -> str:
        return "📄"
    
    def get_description(self) -> str:
        return "No description provided."