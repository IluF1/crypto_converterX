from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Конвертировать 💸')],
    [KeyboardButton(text = 'Показать курс 📈' )],
    [KeyboardButton(text = 'Мой профиль 💻')]

], resize_keyboard = True)

