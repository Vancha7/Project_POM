from base.base_page import BasePage
import allure

class DashboardPage(BasePage):

    _PAGE_URL = "https://www.freeconferencecall.com/profile/account-info-login"
    _INVITE_BUTTON = ("xpath", "//button[@title = 'Пригласить']")

    @allure.step("Клик кнопки Пригласить")
    def click_invite_button(self):
        self.driver.find_element(*self._INVITE_BUTTON).click()