# autotest_project

*Проект автотестов для проверки веб-интерфейсов с использованием Python, Pytest, Selenium и Allure.*

---

## 📋 Структура проекта

```
autotest_project/
│
├── config/                 # Конфиги, настройки тестов
│   ├── config.yaml
│   └── config_reader.py
│
├── fixtures/               # Фикстуры Pytest
│   ├── __init__.py
│   └── conftest.py
│
├── tests/                  # Каталог автотестов
│   ├── __init__.py
│   ├── test_github_advanced_search.py
│   ├── test_github_commit_activity.py
│   ├── test_github_issues_author.py
│   ├── test_sample.py
│   └── test_skillbox_courses.py
│
├── utils/                  # Утилиты, вспомогательные модули
│   ├── __init__.py
│   ├── data_generator.py
│   ├── assert_utils.py
│   ├── browser_utils.py
│   ├── element_helpers.py
│   ├── github_actions.py
│   └── logger.py
│
├── .flake8                 # Конфиг статического анализатора
├── .gitignore              # Игнорируемые git файлы/папки
├── pytest.ini              # Конфиг pytest
├── requirements.txt        # Зависимости проекта
└── README.md               # Этот файл
```

---

## 🚀 Быстрый старт

1. *Клонируй репозиторий:*

   ```sh
   git clone <url-репозитория>
   cd autotest_project
   ```

2. *Создай и активируй виртуальное окружение:*

   ```sh
   python -m venv .venv
   source .venv/bin/activate   # для Linux/Mac
   .venv\Scripts\activate      # для Windows
   ```

3. *Установи зависимости:*

   ```sh
   pip install -r requirements.txt
   ```

---

## 🧪 Запуск тестов

Для запуска всех тестов используй команду:

```sh
pytest
```

Или для генерации отчета Allure:

```sh
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🛠️ Инструменты и стек

- [Python 3.10+](https://www.python.org/)
- [Pytest](https://pytest.org/)
- [Selenium](https://selenium.dev/)
- [Allure](https://docs.qameta.io/allure/)
- [flake8](https://flake8.pycqa.org/) — статический анализатор

---

## 💡 Пример команд

*Запустить только тесты из файла:*
```sh
pytest tests/test_github_advanced_search.py
```

*Проверить стиль кода:*
```sh
flake8
```

---

## 📄 Логирование

Все действия тестов логируются в папке `logs/`, автоматически создаваемой при запуске (см. utils/logger.py).

---

## 🤝 Вклад и поддержка

*Вопросы, предложения и баги — приветствуются через issues или pull-requests!*
