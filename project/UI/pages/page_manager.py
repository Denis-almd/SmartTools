
from project.UI.pages.base_page import BasePage
from project.UI.pages.home.home_page import HomePage
from project.UI.pages.about.about_page_ui import AboutPage
from project.UI.pages.utilizacao_reader.utilizacao_reader import UtilizacaoReader
from project.UI.pages.BDV_consolidado_reader.bdv_consolidado_reader_ui import BDVConsolidadoReaderUI

class PageManager:
    
    _pages: list[type[BasePage]] = [
        HomePage,
        UtilizacaoReader,
        BDVConsolidadoReaderUI,
        AboutPage
    ]
    
    @classmethod
    def get_pages(cls) -> list[type[BasePage]]:
        """Returns new instances of all pages (legacy method)."""
        return [page() for page in cls._pages]
    
    @classmethod
    def get_page_classes(cls) -> list[type[BasePage]]:
        """Returns the page classes (not instances) to allow fresh instantiation."""
        return cls._pages
    
    @classmethod
    def register_page(cls, page: type[BasePage]):
        if page not in cls._pages:
            cls._pages.append(page)