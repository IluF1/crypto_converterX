from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
import app.keyboards as kb
from app.keyboards import cryptocurrencies


router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f'Привет, { message.from_user.first_name }', reply_markup = kb.start_kb)

@router.message(Command('profile'))
@router.message(F.text == 'Мой профиль 💻')
async def profile_handler(message: Message):
    id = 0
    balance = 0
    await message.reply(f"Ваш профиль:\nName: { message.from_user.first_name }\nId: { id }\nBalance: { balance }")


@router.message(Command('course'))
@router.message(F.text == 'Показать курс 📈')
async def course_handler(message: Message):
    if len(cryptocurrencies) > 0:
        await message.reply('Выберите интерисующую криптовалюту:',
            reply_markup = await kb.inline_crypto()
        )
    else:
        await message.reply("Сервис пока что недоступен")