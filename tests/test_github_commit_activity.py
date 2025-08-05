import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utils.logger import setup_logger
import time

logger = setup_logger("test_commit_activity_tooltip")


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def open_commit_activity_page(driver, url):
    logger.info(f"Открываем страницу коммит-активности: {url}")
    driver.get(url)
    time.sleep(3)  # Лучше заменить на явные ожидания


def get_commit_activity_bars(driver):
    logger.info("Получаем элементы графика коммит-активности")
    return driver.find_elements(By.CSS_SELECTOR, '.js-graph-bar')


def hover_over_element(driver, element):
    logger.info("Наводим курсор на первый столбец графика")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)  # Лучше заменить на явные ожидания


def get_tooltip_text(driver):
    logger.info("Получаем текст тултипа графика")
    tooltip = driver.find_element(By.CLASS_NAME, "CommitActivityGraph-tooltip")
    return tooltip.text


@allure.title("Проверка отображения тултипа на графике активности коммитов")
def test_commit_activity_tooltip(driver):
    url = "https://github.com/microsoft/vscode/graphs/commit-activity"

    with allure.step("Открыть страницу графика активности коммитов"):
        open_commit_activity_page(driver, url)

    with allure.step("Получить элементы графика коммит-активности"):
        bars = get_commit_activity_bars(driver)
        logger.info(f"Найдено столбцов на графике: {len(bars)}")
        assert bars, "❌ График не найден!"

    with allure.step("Навести курсор на первый столбец графика"):
        hover_over_element(driver, bars[0])

    with allure.step("Проверить, что тултип содержит слово commit"):
        tooltip_text = get_tooltip_text(driver)
        logger.info(f"Текст тултипа: {tooltip_text}")
        assert "commit" in tooltip_text.lower(), "❌ В тултипе нет слова 'commit'"