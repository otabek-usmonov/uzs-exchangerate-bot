import datetime
import logging
from aiogram import Bot, Dispatcher, executor, types
from currency_rate_info import *


API_TOKEN = '1924029254:AAExLJ4CJ9PZUqNkftXLbuBoibSxb2Stgx8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.answer("Bu botda valyutalarning kodini kiritib, ularning o'zbek so'midagi qiymatini ko'rishingiz mumkin.\n\n\
Botdagi buyruqlar ro'yxatini ko'rish uchun /help ni bosing.")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    commands = "Botdagi buyruqlar ro'yxati:\n\
                /start - Botdan foydalanishni boshlash\n\
                /help - Botdagi buyruqlar ro'yxati\n\
                /currency_code_list - Valyuta kodlarini ko'rish\n\
                /all_rate_ascorder - O'sish tartibida kurslarni ko'rish\n\
                /all_rate_descorder - Kamayish tartibida kurslarni ko'rish"

    await message.answer(commands)


@dp.message_handler(commands=['currency_code_list'])
async def send_currency_codes(message: types.Message):
    """
    This handler will be called when user sends `/currency_code_list` command
    """
    await message.answer(get_currency_codes())


@dp.message_handler(commands=['all_rate_ascorder'])
async def send_currency_codes(message: types.Message):
    """
    This handler will be called when user sends `/all_rate_ascorder` command
    """
    await message.reply(get_ordered_rate_list())


@dp.message_handler(commands=['all_rate_descorder'])
async def send_currency_codes(message: types.Message):
    """
    This handler will be called when user sends `/all_rate_descorder` command
    """
    await message.reply(get_ordered_rate_list(True))


@dp.message_handler()
async def send_rate(message: types.Message):
    currency = message.text.strip().replace("/", "")
    rate = get_rate(currency)

    if not rate:
        if is_currency_code(currency):
            respond = "Bu valyuta kodi uchun ma'lumot yo'q."
        else:
            respond = "Valyuta kodi noto'g'ri kitilgan!"
    else:
        respond = f"Bugungi ({datetime.date.today()}) kurs: 1 {currency} = {rate} UZS"

    await message.answer(respond)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




