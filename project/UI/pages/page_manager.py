
from project.UI.pages.base_page import BasePage
from project.UI.pages.home.home_page import HomePage
from project.UI.pages.about.about_page_ui import AboutPage
#from project.UI.pages.utilizacao_reader.utilizacao_reader_ui import UtilizacaoReader

class PageManager:
    
    _pages: list[type[BasePage]] = [
        HomePage,
        AboutPage
    ]
    
    @classmethod
    def get_pages(cls) -> list[type[BasePage]]:
        return [page() for page in cls._pages]
    
    @classmethod
    def register_page(cls, page: type[BasePage]):
        if page not in cls._pages:
            cls._pages.append(page)