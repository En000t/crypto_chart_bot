import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils import executor
from modules.utils import log_start_stop
from modules.tradingview import fetch_crypto_charts
from config import API_TOKEN

# Налаштування логування
logging.basicConfig(level=logging.INFO, filename='logs/bot.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Ініціалізація бота та диспетчера
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Бот запущено! Використовуйте команду /fetch для отримання даних.")

@dp.message(Command("fetch"))
async def fetch_command(message: types.Message):
    charts = fetch_crypto_charts()
    await message.answer(charts)

@dp.message(Command("stop"))
async def stop_command(message: types.Message):
    await message.answer("Бот зупинено.")
    log_start_stop("Bot stopped")

async def on_startup(dispatcher):
    log_start_stop("Bot started")

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup)
