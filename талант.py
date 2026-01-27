import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = "6738003275:AAHz8vUbrsxPkeZoDE_vmvELuynUXVLDx1M"

WEB_APP_URL = "prof.html"
WEB_APP_URL2 = "https://example.com"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот с веб-приложением.\n\n"
        "Нажмите кнопку ниже, чтобы открыть веб-интерфейс:",
    )


@dp.message(Command("prof"))
async def cmd_webapp(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👨🏼‍❤️‍💋‍👨🏼 ПРОФИЛЬ",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ]
    )
    await message.answer(
        "Я ЧТО ПОХОЖ НА АБОНЕНТА",
        reply_markup=keyboard
    )

@dp.message(Command("pay"))
async def cmd_webapp(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🤑 ОПЛАТА",
                    web_app=WebAppInfo(url=WEB_APP_URL2)
                )
            ]
        ]
    )
    await message.answer(
        "ДЕНЬГИ СБДА ДАВАЙ",
        reply_markup=keyboard
    )

async def main():
    """Запуск бота"""
    # Пропускаем накопленные обновления и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())



#6738003275:AAHz8vUbrsxPkeZoDE_vmvELuynUXVLDx1M


