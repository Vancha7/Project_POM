from pages.base_page import BasePage  # импорт BasePage в данный класс LoginPage

# Класс страницы
class LoginPage(BasePage):  # Наследование от BasePage

    # URL-страницы
    PAGE_URL = "https://example.com"

    # Локаторы страницы
    LOGIN_FIELD = ("xpath", "//input[@id='login']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON = ("xpath", "//button[@id='login-button']")

    # Методы для страницы
    def enter_login(self):
        self.driver.find_element(*self.LOGIN_FIELD).send_keys("example@gmail.com")

    def enter_password(self):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys("qwerty")

    def enter_login_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()