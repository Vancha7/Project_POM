import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия драйвера"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # ВАЖНО: создаем драйвер правильно
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # ВАЖНО: возвращаем драйвер через yield
    yield driver

    # Закрываем драйвер
    driver.quit()