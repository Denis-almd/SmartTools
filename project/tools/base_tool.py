from abc import ABC, abstractmethod

class BaseTool(ABC):
    
    @abstractmethod
    def get_name(self) -> str:
        """Return the name of the tool."""
        pass
    
    @abstractmethod
    def get_icon(self) -> str:
        """Return the icon representing the tool."""
        pass
    
    @abstractmethod
    def render(self):
        """Render the tool's UI components."""
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """Return a brief description of the tool."""
        pass
    
    def get_tab_label(self) -> str:
        """Return the label for the tool's tab."""
        return f"{self.get_name()} {self.get_icon()}"