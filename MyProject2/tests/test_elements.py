import time
import allure
from MyProject2.base.base_test import BaseTest

@allure.epic("Elements1")

class TestElements(BaseTest):

    @allure.step("Click Elements in Open page")
    def test_elements(self):
        self.elements_page.open_page()
        self.elements_page.click_element()
        self.elements_page.click_text_box()
        time.sleep(5)
