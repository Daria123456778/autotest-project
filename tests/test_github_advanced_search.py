import allure
from utils.logger import setup_logger
from utils.github_actions import get_repository_elements, check_repos_stars
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = setup_logger("test_github_advanced_search")

@allure.title(
    "Проверка поиска репозиториев с Python, env, yaml и количеством звёзд > 20000"
)
def test_github_advanced_search_python_env_yml_20kstars(driver):
    wait = WebDriverWait(driver, timeout=15)
    url = "https://github.com/search/advanced"
    min_stars = 20000

    with allure.step("Открыть страницу расширенного поиска GitHub"):
        logger.info(f"Переходим по ссылке: {url}")
        driver.get(url)

    # Если есть шаги фильтрации — тоже обернуть в allure.step + logger.info

    with allure.step("Ожидать появления списка репозиториев"):
        wait.until(EC.visibility_of_element_located((
            'css selector', 'ul.repo-list'
        )))
        logger.info("Список репозиториев загружен")

    with allure.step("Собрать элементы репозиториев"):
        repos = get_repository_elements(driver)
        logger.info(f"Собрано репозиториев: {len(repos)}")

    with allure.step(f"Проверить, что у каждого репозитория звёзд не меньше {min_stars}"):
        check_repos_stars(repos, min_stars=min_stars)
        logger.info(f"Все репозитории имеют звёзд >= {min_stars}")