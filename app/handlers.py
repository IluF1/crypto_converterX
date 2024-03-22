from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
import app.keyboards as kb
from app.keyboards import cryptocurrencies
from app.server.cryptocurrencies import crypto_price
from datetime import datetime

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.start_kb)

# @router.message(Command('conversion'))
# @router.message(F.text == 'Конвертировать 💸')
# async def conversion_handler(message: Message):
#     if cryptocurrencies:
#         await message.reply('Выберите какую криптовалюту вы хотите получить:', reply_markup=await kb.inline_crypto_conversion())
#     else:
#         await message.reply("Сервис пока что недоступен")

@router.message(Command('course'))
@router.message(F.text == 'Показать курс 📈')
async def course_handler(message: Message):
    if cryptocurrencies:
        await message.reply('Выберите интересующую криптовалюту:', reply_markup=await kb.inline_crypto())
    else:
        await message.reply("Сервис пока что недоступен")

# @router.callback_query(lambda query: query.data in cryptocurrencies)
# async def cryptocurrency_course_format(callback: CallbackQuery):
#     selected_cryptocurrency = callback.data
#     if 'conversion' in selected_cryptocurrency:
#         selected_cryptocurrency_format = selected_cryptocurrency.split('conversion')[0]
#         await callback.message.reply(selected_cryptocurrency_format)

@router.callback_query(lambda query: query.data in cryptocurrencies)
async def cryptocurrency_course_price(callback: CallbackQuery):
    selected_cryptocurrency = callback.data
    crypto = crypto_price(selected_cryptocurrency)
    nowdate = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    await callback.message.reply(f"Курс {selected_cryptocurrency} на {nowdate}: {crypto}$ за штуку")
