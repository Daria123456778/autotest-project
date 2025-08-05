import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger

logger = setup_logger("test_github_issues_filter_by_author")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def open_issues_page(driver, wait):
    logger.info("Открываем страницу задач VS Code на Github")
    driver.get('https://github.com/microsoft/vscode/issues')
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))


def filter_by_author(driver, wait, author_name):
    logger.info(f"Фильтруем задачи по автору: {author_name}")
    # Нажимаем кнопку "Author"
    author_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="author-filter-menu"]')))
    author_btn.click()

    # Вводим имя
    author_input = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="author-filter-input"]'))
    )
    author_input.clear()
    author_input.send_keys(author_name)

    # Ждём и кликаем по нужному автору
    author_option = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, f'//button[contains(@data-testid,"author-option-") and contains(.,"{author_name}")]')
        )
    )
    author_option.click()


def get_issue_authors(driver, wait):
    logger.info("Получаем список авторов задач")
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="issue-list-container"]'))
    )
    return driver.find_elements(By.CSS_SELECTOR, 'a[data-testid="issue-author-link"]')


def check_issues_authors(issues, author_name):
    logger.info(f"Проверяем, что все задачи от автора {author_name}")
    for i, issue_author in enumerate(issues, 1):
        assert author_name.lower() in issue_author.text.lower(), (
            f'Ошибка: задача #{i} не от автора {author_name}!'
        )
        logger.info(f'Задача #{i}: OK ({issue_author.text})')
    logger.info(f'✅ Все задачи от автора {author_name}')


@allure.title("Проверка фильтрации задач по автору на Github")
def test_github_issues_filter_by_author(driver):
    wait = WebDriverWait(driver, 15)
    author_name = 'bpasero'

    with allure.step("Открыть страницу задач VS Code на Github"):
        open_issues_page(driver, wait)
    with allure.step(f"Отфильтровать задачи по автору {author_name}"):
        filter_by_author(driver, wait, author_name)
    with allure.step("Получить список авторов задач"):
        issues = get_issue_authors(driver, wait)
    with allure.step(f"Проверить, что все задачи написаны автором {author_name}"):
        check_issues_authors(issues, author_name)
