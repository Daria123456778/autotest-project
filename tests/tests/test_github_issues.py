import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_search_issues_with_bug_in_title():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    try:
        url = "https://github.com/microsoft/vscode/issues"
        driver.get(url)

        # 2. Вводим фильтр по инпуту поиска
        search_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search all issues"]')
        search_input.clear()
        search_input.send_keys('in:title bug')
        search_input.send_keys(Keys.ENTER)

        # 3-5. Получаем названия задач c bug в заголовке (регистр не важен)
        issue_titles = driver.find_elements(By.CSS_SELECTOR, 'a.Link--primary.v-align-middle.no-underline.h4.js-navigation-open.markdown-title')

        # Проверяем, что каждый заголовок содержит слово "bug" (без учёта регистра)
        assert issue_titles, "Не найдено ни одной задачи."
        for title_elem in issue_titles:
            title_text = title_elem.text.lower()
            assert "bug" in title_text, f'В заголовке не найдено "bug": {title_text}'
    finally:
        driver.quit()