import pytest
from pages.login_page import LoginPage
import time


class TestLoginPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)

    def test_login_in_account(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.enter_login_button()
        time.sleep(5)