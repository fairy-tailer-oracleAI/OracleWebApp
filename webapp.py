from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import WebAppInfo, WebAppData
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

API_TOKEN = "6880883452:AAEdgb_Azu4BOr19RsSpf8s-ryXm7rpXxBw"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    # Создаем инлайн кнопку
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Открыть веб-приложение",
        web_app=types.WebAppInfo(url="https://fairy-tailer-oracleai.github.io/OracleWebApp/")
    )
    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы открыть веб-приложение.",
        reply_markup=builder.as_markup()
    )

# Обработчик данных от веб-приложения
@dp.message(WebAppData)
async def web_app_data_handler(message: types.Message):
    # Получаем данные, отправленные из веб-приложения
    data = message.web_app_data.data
    await message.answer(f"Вы выбрали следующие карты: {data}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

#https://mariatarobot.com/webapp/?lang=ru&deck=taro#tgWebAppData=query_id%3DAAH2qjpMAgAAAPaqOkxl-MXQ%26user%3D%257B%2522id%2522%253A5573880566%252C%2522first_name%2522%253A%2522%25D0%25B8%25D0%25BB%25D1%258C%25D1%258F%2520%2528IKA%2529%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522osk_skilz%2522%252C%2522language_code%2522%253A%2522ru%2522%252C%2522is_premium%2522%253Atrue%252C%2522allows_write_to_pm%2522%253Atrue%252C%2522photo_url%2522%253A%2522https%253A%255C%252F%255C%252Ft.me%255C%252Fi%255C%252Fuserpic%255C%252F320%255C%252FLIsmmI8TxqFtE1Gjd1_lm4BuIuVxj1nNRx6DNw4ujb6_88s-wUQNghFg3Lxb_5gD.svg%2522%257D%26auth_date%3D1745254252%26signature%3DKAt8lINUgT8gw2cYI125-LkXnJG5VEgbKO495Vm7HDL5b57NmLHhFcQ_xiK9kAANZ-HF0EzeN5370vxWR8FKDQ%26hash%3Dc82a5761b235ac5f1bf34f96501a55d273164ee515319dd998be127aab8ae689&tgWebAppVersion=8.0&tgWebAppPlatform=weba&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23212121%22%2C%22text_color%22%3A%22%23ffffff%22%2C%22hint_color%22%3A%22%23aaaaaa%22%2C%22link_color%22%3A%22%238774e1%22%2C%22button_color%22%3A%22%238774e1%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22secondary_bg_color%22%3A%22%230f0f0f%22%2C%22header_bg_color%22%3A%22%23212121%22%2C%22accent_text_color%22%3A%22%238774e1%22%2C%22section_bg_color%22%3A%22%23212121%22%2C%22section_header_text_color%22%3A%22%23aaaaaa%22%2C%22subtitle_text_color%22%3A%22%23aaaaaa%22%2C%22destructive_text_color%22%3A%22%23e53935%22%7D