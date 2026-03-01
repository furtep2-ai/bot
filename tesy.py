import aiogram 
from aiogram import Bot , Dispatcher
from aiogram.types import Message , BotCommand , ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardMarkup, InlineKeyboardButton, callback_query
from aiogram.filters import Command
from aiogram import types
import asyncio
from ter23 import TOKEN

bot=Bot(token=TOKEN)


dp=Dispatcher()

inline=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='IT' , callback_data='button1')],
    [InlineKeyboardButton(text='Педагогика' , callback_data='button2')],
    [InlineKeyboardButton(text='Экономика' , callback_data='button3')],
    [InlineKeyboardButton(text='Медицина',callback_data='button4')]
    ]
)
inline2=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Список документов' , callback_data='btn1')],
    [InlineKeyboardButton(text='Стоимость' , callback_data='btn2')],
    [InlineKeyboardButton(text='FAQ' , callback_data='btn3')]
    ]
)

inline3=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Да" , callback_data="yes")],
    [InlineKeyboardButton(text="Нет" , callback_data="no")]
])

@dp.message(Command("start"))
async def start(message:Message):
    await message.answer("Здравствуйте узнать информацию о поступлении используйте /help")
@dp.message(Command("help"))
async def help(message:Message):
    await message.answer(" Привет! На 2026 год прием с 20 июня. Выберите факультет:",reply_markup=inline)
@dp.callback_query()
async def accept(callback:types.CallbackQuery):
    if callback.data=="button1" or callback.data=="button2" or callback.data=="button3" or callback.data=="button4":
        await callback.message.answer("Нужны: аттестат, сертификат ЕНТ (мин. 65 баллов), паспорт. " \
        "Загрузите файлы или ссылка: aogu.edu.kz/abiturient",reply_markup=inline2)

    if callback.data=="btn1" or callback.data=="btn2" or callback.data=="btn3":
        await callback.message.answer("Бакалавриат — 1,200,000 тг/год (гранты по конкурсу)",reply_markup=inline3)

    if callback.data=="yes" or callback.data=="no":
        await callback.message.answer("Конец")
    await callback.answer()

async def set_commands(bot):
    commands=[
        BotCommand(command="start",description="Здравствуйте узнать информацию о поступлении используйте"),
        BotCommand(command="help",description=" Привет! На 2026 год прием с 20 июня. Выберите факультет:")
    ]
    await bot.set_my_commands(commands)
async def main():
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__=="__main__":
    print("Бот запущен и готов к работе")
    asyncio.run(main())
    