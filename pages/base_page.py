from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    # Тут описываются локаторы
    LOGOUT_BUTTON = ("xpath", "//button[@id='logout']")
    LOGO = ("xpath", "//a[@id='logo']")

    # Тут создаются объекты, которые будут доступны в pages
    def __init__(self, driver):
        self.driver = driver
        # Здесь может быть остальной код

    # Данный метод будет вызываться для любой страницы, принимая её PAGE_URL
    def open(self):
        self.driver.get(self.PAGE_URL)

    # Ниже описываются общие для всех страниц методы
    def click_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()

    def click_logo_link(self):
        self.driver.find_element(*self.LOGO).click()