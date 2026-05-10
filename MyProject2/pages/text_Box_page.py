from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MyProject2.base.base_page import BasePage
import allure

FULL_NAME = "xpath", "//input[@id = 'userName']"

@allure.step("Проверка раздела TextBox")
class TextBoxPage(BasePage):
    def click_text_box(self):
        self.wait.until(EC.presence_of_element_located(FULL_NAME)).send_keys("Иван Васильченко")


