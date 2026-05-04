import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utiles.generator import Generators
from data.credentials import Credentials

class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.data = Credentials()
        self.generator = Generators()
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)
