import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Можно вынести фикстуру браузера отдельно для переиспользования в других тестах
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_github_advanced_search_python_env_yml_20kstars(driver):
    wait = WebDriverWait(driver, 15)
    driver.get('https://github.com/search/advanced')

    # 1. Выбор языка Python
    language_input = wait.until(
        EC.presence_of_element_located((By.ID, 'search_language'))
    )
    language_input.click()
    python_option = driver.find_element(By.XPATH, "//option[@value='Python']")
    python_option.click()

    # 2. Задаём количество звёзд > 20000
    stars_input = driver.find_element(By.ID, 'search_stars')
    stars_input.clear()
    stars_input.send_keys('>20000')

    # 3. Вводим имя файла environment.yml
    filename_input = driver.find_element(By.ID, 'search_filename')
    filename_input.clear()
    filename_input.send_keys('environment.yml')

    # 4. Нажимаем на кнопку поиска
    search_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    search_btn.click()

    # 5. Собираем результаты репозиториев
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.repo-list')))
    repos = driver.find_elements(By.CSS_SELECTOR, 'ul.repo-list li')

    assert repos, "Репозитории не найдены!"

    for repo in repos:
        repo_name = repo.find_element(By.CSS_SELECTOR, 'a.v-align-middle').text
        # Ищем количество звёзд
        try:
            stars_text = repo.find_element(By.CSS_SELECTOR, "a.Link--muted[href$='/stargazers']").text
            stars_num = int(stars_text.replace(",", ""))
            assert stars_num > 20000, f"У репозитория {repo_name} всего {stars_num} звёзд, меньше 20000"
        except Exception as e:
            pytest.fail(f"Не удалось найти или проверить количество звёзд у {repo_name}: {e}")

        print(f"{repo_name}: ⭐️ {stars_text}")

    print("Все найденные репозитории соответствуют фильтру (>20000 звёзд, Python, environment.yml)")
