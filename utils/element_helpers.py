# utils/element_helpers.py

from selenium.webdriver.common.action_chains import ActionChains

def hover_on_element(driver, element):
    """
    Наводит курсор мыши на элемент.
    """
    ActionChains(driver).move_to_element(element).perform()
