from aiogram import Router, F
from aiogram.types import Message,CallbackQuery
from aiogram.filters import Command, CommandStart
import app.keyboards as kb
from app.keyboards import cryptocurrencies
import datetime
from app.server.cryptocurrencies import crypto_price


router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f'Привет, { message.from_user.first_name }', reply_markup = kb.start_kb)


@router.message(Command('course'))
@router.message(F.text == 'Показать курс 📈')
async def course_handler(message: Message):
    if cryptocurrencies:
        await message.reply('Выберите интересующую криптовалюту:',
            reply_markup = await kb.inline_crypto()
        )
    else:
        await message.reply("Сервис пока что недоступен")

@router.callback_query(lambda query: query.data in cryptocurrencies)
async def cryptocurrency(callback: CallbackQuery):
    selected_cryptocurrency = callback.data
    crypto = crypto_price(selected_cryptocurrency)

    nowdate = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    await callback.message.reply(f"Курс {selected_cryptocurrency} на {nowdate}: {crypto}$ за штуку")