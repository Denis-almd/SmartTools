from abc import ABC, abstractmethod

class BasePage(ABC):
    
    @abstractmethod
    def render(self):
        """Render the page's UI components."""
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        """Return the name of the page."""
        pass
    
    def get_icon(self) -> str:
        """Return the icon representing the page."""
        return "📄"
    
    def get_description(self) -> str:
        """Return a brief description of the page."""
        return "No description provided."