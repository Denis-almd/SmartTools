from project.tools.base_tool import BaseTool
from project.tools.time_converter.time_converter_ui import TimeConverter
from project.tools.password_generator.password_generator import Password_generator

class ToolRegister:
    _tools: list[type[BaseTool]] = [
        TimeConverter,
        Password_generator
        ]
    
    @classmethod
    def get_tools(cls) -> list[BaseTool]:
        return [tool() for tool in cls._tools]
    
    @classmethod
    def register_tool(cls, class_tool: type[BaseTool]):
        if issubclass(class_tool, BaseTool) and class_tool not in cls._tools:
            cls._tools.append(class_tool)