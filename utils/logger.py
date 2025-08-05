import logging
import os

def setup_logger(log_name):
    # Папка для логов (по желанию)
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f"{log_name}.log")

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)

    # Формат логов
    formatter = logging.Formatter(
        "[%(asctime)s][%(levelname)s] - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Проверяем, добавлен ли уже обработчик, чтобы избежать дублирования логов
    if not logger.handlers:
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger