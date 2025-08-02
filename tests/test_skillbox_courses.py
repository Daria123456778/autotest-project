import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_skillbox_courses_filter(driver):
    wait = WebDriverWait(driver, 20)
    # 1. Открыть главный каталог курсов по программированию от Skillbox
    driver.get("https://skillbox.ru/code/")

    # 2. Выбрать профессию в разделе "Тип обучения" (пример селектора)
    profession_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Профессии')]"))
    )
    profession_btn.click()

    # 3. Фильтр по длительности: задаём диапазон от 6 до 12 месяцев
    # (На сайте может быть ползунок, нужен drag&drop или клик по "6" и "12". Пример: найдём ползунки по data-attribute)
    # ДЛЯ ПРИМЕРА! Возможно, потребуется уточнить селектор под реальную верстку:
    duration_min = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='range' and @aria-label='Минимальная длительность']"))
    )
    duration_max = driver.find_element(By.XPATH, "//input[@type='range' and @aria-label='Максимальная длительность']")
    # Пример простого действия (посложнее — через ActionChains)
    duration_min.send_keys("6")
    duration_max.send_keys("12")

    # 4. В теме выбрать любой чекбокс (например, веб-разработка)
    # Найдем первый доступный чекбокс для темы и кликнем:
    theme_checkbox = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']"))
    )
    theme_checkbox.click()

    # 5. Проверить, что курсы в списке отображаются (просто пример проверки наличия)
    course_cards = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-course-id]"))
    )
    assert len(course_cards) > 0, "Нет курсов по выбранным фильтрам!"

    # По желанию: сравнить названия курсов с ожидаемыми (пример):
    course_names = [card.text for card in course_cards]
    print("Найденные курсы:", course_names)


