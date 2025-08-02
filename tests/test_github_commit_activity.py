import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    # Используй путь к chromedriver, если он не прописан в PATH
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_commit_activity_tooltip(driver):
    url = "https://github.com/microsoft/vscode/graphs/commit-activity"
    driver.get(url)
    time.sleep(3)  # Ждём загрузки графика

    # Находим первый столбик на графике (селектор может отличаться, если что — поправь)
    bars = driver.find_elements(By.CSS_SELECTOR, ".js-graph-bar")
    assert bars, "График не найден!"

    # Наводим мышку на первый столбик
    actions = ActionChains(driver)
    actions.move_to_element(bars[0]).perform()
    time.sleep(1)

    # Находим тултип
    tooltip = driver.find_element(By.CLASS_NAME, "CommitActivityGraph-tooltip")
    tooltip_text = tooltip.text
    print("Текст тултипа:", tooltip_text)

    # Проверяем, что в тултипе есть слово "commits"
    assert "commit" in tooltip_text.lower()