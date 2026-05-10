from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MyProject2.base.base_page import BasePage
import allure

class ElementsPage(BasePage):

    ELEMENTS = ("xpath", "//div[@class= 'card-body']")
    TEXT_BOX = ("xpath", "//span[@class = 'text']")
    PAGE_URL = "https://demoqa.com"

    def __init__(self, driver):
       super().__init__(driver)

    @allure.step("Переход в Elements")
    def click_element(self):
        self.wait.until(EC.element_to_be_clickable(self.ELEMENTS)).click()

    @allure.step("Открыт раздел Elements")
    def click_text_box(self):
        self.wait.until(EC.element_to_be_clickable(self.TEXT_BOX)).click()
