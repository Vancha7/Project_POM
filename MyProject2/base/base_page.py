from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:

    PAGE_URL = None

    # Тут создаются объекты, которые будут доступны в pages
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        # Здесь может быть остальной код

    # Данный метод будет вызываться для любой страницы, принимая её PAGE_URL
    @allure.step("Open PAGE")
    def open_page(self):
        with allure.step(F"Open {self.PAGE_URL} PAGE"):
          self.driver.get(self.PAGE_URL)