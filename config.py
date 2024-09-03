import os
from dotenv import load_dotenv

# Завантаження змінних середовища з файлу .env
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

# Перевірка, чи встановлений API_TOKEN
if not API_TOKEN:
    raise ValueError("API_TOKEN не знайдено в змінних середовища")

CRYPTO_PAIRS = [
    "BTC/USDT",
    "ETH/USDT",
    "BNB/USDT",
    # Додайте інші пари криптовалют тут
]
