from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f'Привет, { message.from_user.first_name }', reply_markup = kb.start_kb)



@router.message(Command('help'))
@router.message(F.text == 'Помощь ✨')
async def help_handler(message: Message):
    await message.reply('Привет')