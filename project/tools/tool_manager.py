from project.tools.base_tool import BaseTool
from project.tools.time_converter.time_converter_ui import TimeConverter

class ToolRegister:
    _tools: list[type[BaseTool]] = [
        TimeConverter,
        ]
    
    @classmethod
    def get_tools(cls) -> list[BaseTool]:
        return [tool() for tool in cls._tools]
    
    @classmethod
    def register_tool(cls, class_tool: type[BaseTool]):
        if issubclass(class_tool, BaseTool) and class_tool not in cls._tools:
            cls._tools.append(class_tool)