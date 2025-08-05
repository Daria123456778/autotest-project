import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger

logger = setup_logger("test_github_issues_search_by_keyword")


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def open_issues_page(driver, wait):
    logger.info("Открываем страницу задач VS Code на Github")
    url = 'https://github.com/microsoft/vscode/issues'
    driver.get(url)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))


def enter_filter(driver, wait, keyword):
    logger.info(f"Вводим фильтр поиска: in:title {keyword}")
    search_input = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search all issues"]'))
    )
    search_input.clear()
    search_input.send_keys(f'in:title {keyword}')
    search_input.send_keys(Keys.ENTER)


def get_issue_titles(driver, wait):
    logger.info("Получаем заголовки найденных задач")
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="issue-list-container"]'))
    )
    return [
        e.text for e in driver.find_elements(By.CSS_SELECTOR, 'a[data-hovercard-type="issue"]')
        if e.text.strip()
    ]


def check_titles_for_keyword(titles, keyword):
    logger.info(f'Проверяем, что все задачи содержат "{keyword}" в заголовке')
    for i, title in enumerate(titles, 1):
        assert keyword.lower() in title.lower(), (
            f"Ошибка: задача №{i} не содержит слово '{keyword}'! Заголовок: {title}"
        )
        logger.info(f'Задача №{i}: OK ("{title}")')


@allure.title('Проверка поиска задач по ключевому слову в заголовке на Github')
def test_github_issues_search_by_keyword(driver):
    wait = WebDriverWait(driver, 15)
    keyword = 'bug'

    with allure.step("Открыть страницу задач VS Code на Github"):
        open_issues_page(driver, wait)
    with allure.step(f"Ввести фильтр in:title {keyword} и отправить поисковый запрос"):
        enter_filter(driver, wait, keyword)
    with allure.step("Получить все заголовки найденных задач"):
        titles = get_issue_titles(driver, wait)
        logger.info(f'Найдено задач: {len(titles)}')
        assert titles, "❌ Не найдено ни одной задачи!"
    with allure.step(f"Проверить, что каждая задача содержит слово '{keyword}' в заголовке"):
        check_titles_for_keyword(titles, keyword)
