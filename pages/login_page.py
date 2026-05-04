from base.base_page import BasePage  # импорт BasePage в данный класс LoginPage
import allure

# Класс страницы
class LoginPage(BasePage):  # Наследование от BasePage

    # URL-страницы
    PAGE_URL = "https://www.freeconferencecall.com/ru/ru/login"

    # Локаторы страницы
    LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

    def __init__(self, driver):
        super().__init__(driver)

    # Методы для страницы
    @allure.step("Enter email")
    def enter_login(self, login):
        self.driver.find_element(*self.LOGIN_FIELD).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    @allure.step("enter_button")
    def enter_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()