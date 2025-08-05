import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger

logger = setup_logger("test_skillbox_courses_filter")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def open_skillbox_courses_page(driver, wait):
    logger.info("Открываем страницу курсов Skillbox")
    driver.get("https://skillbox.ru/code/")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))


def select_profession_tab(wait):
    logger.info("Выбираем вкладку 'Профессии'")
    profession_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Профессии')]"))
    )
    profession_btn.click()


def set_duration_filter(wait, driver, min_val="6", max_val="12"):
    logger.info(f"Устанавливаем фильтр по длительности: от {min_val} до {max_val} месяцев")
    duration_min = wait.until(
        EC.element_to_be_clickable((
            By.XPATH, "//input[@type='range' and @aria-label='Минимальная длительность']"
        ))
    )
    duration_max = driver.find_element(
        By.XPATH, "//input[@type='range' and @aria-label='Максимальная длительность']"
    )
    duration_min.send_keys(min_val)
    duration_max.send_keys(max_val)


def select_first_theme_checkbox(wait):
    logger.info("Выбираем первую тему курсов")
    theme_checkbox = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']"))
    )
    theme_checkbox.click()


def get_course_cards(wait):
    logger.info("Получаем найденные курсы")
    return wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-course-id]"))
    )


@allure.title("Проверка фильтрации курсов Skillbox по параметрам")
def test_skillbox_courses_filter(driver):
    wait = WebDriverWait(driver, 20)
    with allure.step("Открываем страницу курсов Skillbox"):
        open_skillbox_courses_page(driver, wait)
    with allure.step("Выбираем вкладку 'Профессии'"):
        select_profession_tab(wait)
    with allure.step("Устанавливаем фильтр по длительности курсов"):
        set_duration_filter(wait, driver)
    with allure.step("Выбираем первую тему курсов"):
        select_first_theme_checkbox(wait)
    with allure.step("Получаем и проверяем найденные курсы"):
        course_cards = get_course_cards(wait)
        logger.info(f"Найдено курсов: {len(course_cards)}")
        assert len(course_cards) > 0, "❌ Нет курсов по выбранным фильтрам!"
        course_names = [card.text for card in course_cards]
        logger.info(f"Список найденных курсов: {course_names}")