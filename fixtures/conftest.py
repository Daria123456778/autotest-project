import pytest
from selenium import webdriver
import os
from config.config_reader import load_config

# Фикстура для загрузки настроек (config.yaml)
@pytest.fixture(scope="session")
def config():
    config_path = os.path.join(os.path.dirname(__file__), "../config/config.yaml")
    return load_config(config_path)

# Фикстура для запуска браузера
@pytest.fixture(scope="function")
def browser(config, request):
    browser_name = config.get("browser", "chrome")
    headless = config.get("headless", False)
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Browser {browser_name} is not implemented in fixtures!")
    yield driver
    driver.quit()


import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()