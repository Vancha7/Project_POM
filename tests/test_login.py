import time
import allure
from base.base_test import BaseTest
from data.credentials import Credentials

@allure.epic("User")
@allure.feature("Login")
class TestLoginPage(BaseTest):

    @allure.step("Login in account")
    def test_login_in_account(self):
        self.login_page.open()
        self.login_page.enter_login(Credentials.LOGIN)
        self.login_page.enter_password(Credentials.PASSWORD)
        self.login_page.enter_login_button()
        time.sleep(5)
        self.dashboard_page.click_invite_button()
        time.sleep(3)