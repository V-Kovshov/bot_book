from aiogram import Router
from aiogram.types import Message

router: Router = Router()

# Хэндлер реагирует на любые сообщения пользователя, которые не предусмотрены работой бота
@router.message()
async def send_echo(message: Message):
    await message.answer(f'Это эхо! {message.text}')
