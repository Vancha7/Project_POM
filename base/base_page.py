from selenium.webdriver.chrome.webdriver import WebDriver
import allure

class BasePage:

    # Тут описываются локаторы
    LOGOUT_BUTTON = ("xpath", "//button[@id='logout']")
    LOGO = ("xpath", "//a[@id='logo']")

    PAGE_URL = None

    # Тут создаются объекты, которые будут доступны в pages
    def __init__(self, driver):
        self.driver: WebDriver = driver
        # Здесь может быть остальной код

    # Данный метод будет вызываться для любой страницы, принимая её PAGE_URL
    @allure.step("Open PAGE")
    def open(self):
        with allure.step(F"Open {self.PAGE_URL} PAGE"):
          self.driver.get(self.PAGE_URL)

    # Ниже описываются общие для всех страниц методы
    def click_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def click_logo_link(self):
        self.driver.find_element(*self.LOGO).click()