import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure

from utils.logger import setup_logger
from utils.github_actions import search_issues, get_issues_titles

# Логгер, имя файла зависит от теста
logger = setup_logger("test_search_issues")

@allure.title("Проверка поиска задач с 'bug' в заголовке на Github")
def test_search_issues_with_bug_in_title():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    try:
        url = "https://github.com/microsoft/vscode/issues"
        with allure.step("Открыть страницу с задачами VS Code на Github"):
            logger.info(f"Переходим по ссылке: {url}")
            driver.get(url)

        with allure.step("Выполнить поиск задач с 'bug' в заголовке"):
            logger.info("Выполняется поиск по фильтру: in:title bug")
            search_issues(driver, 'in:title bug')

        with allure.step("Получить заголовки найденных задач"):
            issue_titles = get_issues_titles(driver)
            logger.info(f"Найдено задач: {len(issue_titles)}")
            assert issue_titles, "❌ Не найдено ни одной задачи."

        with allure.step("Проверить, что в каждом заголовке есть слово 'bug'"):
            for title_elem in issue_titles:
                title_text = title_elem.text.lower()
                logger.info(f"Проверка заголовка: {title_text}")
                assert "bug" in title_text, (
                    f'❌ В заголовке не найдено "bug": {title_text}'
                )

    finally:
        driver.quit()
        logger.info("Драйвер закрыт успешно")
