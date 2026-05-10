import pytest
from MyProject2.pages.elements_page import ElementsPage

class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.elements_page = ElementsPage(self.driver)
