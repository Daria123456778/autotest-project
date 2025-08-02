import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)
driver.get('https://github.com/microsoft/vscode/issues')

# 1. Нажимаем кнопку "Author"
author_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="author-filter-menu"]'))
)
author_btn.click()

# 2. Вводим имя автора
author_name = 'bpasero'
author_input = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-testid="author-filter-input"]'))
)
author_input.clear()
author_input.send_keys(author_name)

# 3. Ждём появления и выбираем нужного автора
author_option = wait.until(
    EC.visibility_of_element_located((
        By.XPATH, f'//button[contains(@data-testid,"author-option-") and contains(.,"{author_name}")]'
    ))
)
author_option.click()

# 4. Получаем все задачи
wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="issue-list-container"]'))
)
issues = driver.find_elements(By.CSS_SELECTOR, 'a[data-testid="issue-author-link"]')

# 5. Проверяем каждого автора
for i, issue_author in enumerate(issues, 1):
    assert author_name.lower() in issue_author.text.lower(), f'Ошибка: задача #{i} не этого автора!'
    print(f'Задача #{i}: OK ({issue_author.text})')

print('✅ Все задачи — от автора', author_name)
# driver.quit()