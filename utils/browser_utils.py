# utils/browser_utils.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, by, locator, timeout=10):
    """
    Ждёт появления элемента на странице.
    """
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, locator))
    )

def scroll_to_element(driver, element):
    """
    Скроллит страницу к нужному элементу.
    """
    driver.execute_script("arguments[0].scrollIntoView();", element)