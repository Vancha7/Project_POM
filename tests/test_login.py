import time

from base.base_test import BaseTest


class TestLoginPage(BaseTest):

    def test_login_in_account(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.enter_login_button()
        time.sleep(5)
        self.dashboard_page.click_invite_button()
        time.sleep(3)