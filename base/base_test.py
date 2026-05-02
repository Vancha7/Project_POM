import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)
