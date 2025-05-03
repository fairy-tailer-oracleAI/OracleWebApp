import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice
from aiogram.utils.keyboard import InlineKeyboardBuilder
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token='6880883452:AAEdgb_Azu4BOr19RsSpf8s-ryXm7rpXxBw')  # Замените на ваш токен бота
dp = Dispatcher()

# Команда /start
@dp.message(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Оплатить 10 Stars", callback_data="pay")
    await message.answer(
        "Привет! Это бот для оплаты 10 Telegram Stars. Нажми кнопку ниже, чтобы оплатить.",
        reply_markup=keyboard.as_markup()
    )

# Обработка нажатия на кнопку оплаты
@dp.callback_query(lambda c: c.data == 'pay')
async def process_pay(callback: types.CallbackQuery):
    # Создание инвойса
    prices = [LabeledPrice(label='Оплата', amount=10)]  # 10 Stars
    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title='Оплата 10 Telegram Stars',
        description='Оплата за доступ к эксклюзивному контенту',
        payload='payment_10_stars',
        provider_token='',  # Для Telegram Stars не требуется provider_token
        currency='XTR',  # Валюта Telegram Stars
        prices=prices,
        start_parameter='payment'
    )

# Обработка предпроверки платежа
@dp.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# Обработка успешной оплаты
@dp.message(content_types=['successful_payment'])
async def process_successful_payment(message: types.Message):
    await message.answer(
        "Оплата прошла успешно! Спасибо за покупку 10 Stars! 🎉"
    )

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

#https://mariatarobot.com/webapp/?lang=ru&deck=taro#tgWebAppData=query_id%3DAAH2qjpMAgAAAPaqOkxl-MXQ%26user%3D%257B%2522id%2522%253A5573880566%252C%2522first_name%2522%253A%2522%25D0%25B8%25D0%25BB%25D1%258C%25D1%258F%2520%2528IKA%2529%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522osk_skilz%2522%252C%2522language_code%2522%253A%2522ru%2522%252C%2522is_premium%2522%253Atrue%252C%2522allows_write_to_pm%2522%253Atrue%252C%2522photo_url%2522%253A%2522https%253A%255C%252F%255C%252Ft.me%255C%252Fi%255C%252Fuserpic%255C%252F320%255C%252FLIsmmI8TxqFtE1Gjd1_lm4BuIuVxj1nNRx6DNw4ujb6_88s-wUQNghFg3Lxb_5gD.svg%2522%257D%26auth_date%3D1745254252%26signature%3DKAt8lINUgT8gw2cYI125-LkXnJG5VEgbKO495Vm7HDL5b57NmLHhFcQ_xiK9kAANZ-HF0EzeN5370vxWR8FKDQ%26hash%3Dc82a5761b235ac5f1bf34f96501a55d273164ee515319dd998be127aab8ae689&tgWebAppVersion=8.0&tgWebAppPlatform=weba&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23212121%22%2C%22text_color%22%3A%22%23ffffff%22%2C%22hint_color%22%3A%22%23aaaaaa%22%2C%22link_color%22%3A%22%238774e1%22%2C%22button_color%22%3A%22%238774e1%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22secondary_bg_color%22%3A%22%230f0f0f%22%2C%22header_bg_color%22%3A%22%23212121%22%2C%22accent_text_color%22%3A%22%238774e1%22%2C%22section_bg_color%22%3A%22%23212121%22%2C%22section_header_text_color%22%3A%22%23aaaaaa%22%2C%22subtitle_text_color%22%3A%22%23aaaaaa%22%2C%22destructive_text_color%22%3A%22%23e53935%22%7D