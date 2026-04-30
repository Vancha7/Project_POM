from pages.login_page import LoginPage


class TestLoginPage:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)

    def test_login_in_account(self):
        self.login_page.open()
        self.login_page.enter_login()
        self.login_page.enter_password()
        self.login_page.enter_login_button()