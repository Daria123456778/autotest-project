# utils/github_actions.py
from selenium.webdriver.common.by import By

def get_repository_elements(driver):
    """Возвращает список элементов-репозиториев на странице поиска Github."""
    return driver.find_elements(By.CSS_SELECTOR, 'ul.repo-list li')

def get_repository_name(repo_elem):
    """Возвращает название репозитория (или любой другой нужный атрибут)."""
    return repo_elem.find_element(By.CSS_SELECTOR, 'a.v-align-middle').text

def get_stars_count(repo_elem):
    """Возвращает количество звёзд у репозитория (int)."""
    stars_text = repo_elem.find_element(By.CSS_SELECTOR, "[aria-label*='star']").text
    stars_text = stars_text.replace(',', '').replace(' ', '')
    if 'k' in stars_text.lower():
        stars_num = float(stars_text.lower().replace('k', '')) * 1000
    else:
        stars_num = int(stars_text)
    return int(stars_num)

def check_repos_stars(repos, min_stars=20000):
    """Проверяет, что у всех переданных репозиториев не менее min_stars."""
    import pytest
    assert repos, "Репозитории не найдены!"
    for repo_elem in repos:
        repo_name = get_repository_name(repo_elem)
        try:
            stars_num = get_stars_count(repo_elem)
            assert stars_num >= min_stars, (
                f'В репозитории {repo_name} всего {stars_num} звезд, меньше {min_stars}!'
            )
            print(f'{repo_name}: ⭐ {stars_num}')
        except Exception as e:
            pytest.fail(f"Не удалось найти или проверить количество звезд у {repo_name}: {e}")
    print(f"Все найденные репозитории соответствуют фильтру (> {min_stars} звёзд)!")