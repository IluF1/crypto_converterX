from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.server.cryptocurrencies import cryptocurrencies_request


start_kb = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Конвертировать 💸')],
    [KeyboardButton(text = 'Мой профиль 💻')]

], resize_keyboard = True)

cryptocurrencies = cryptocurrencies_request()

async def inline_crypto():
    keyboard = InlineKeyboardBuilder()
    for cryptocurrency in cryptocurrencies:
        keyboard.add(InlineKeyboardButton(text = cryptocurrency, callback_data = cryptocurrency, ))
    return keyboard.adjust(2).as_markup()