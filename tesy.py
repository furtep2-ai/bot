import aiogram 
from aiogram import Bot , Dispatcher
from aiogram.types import Message , BotCommand , ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardMarkup, InlineKeyboardButton, callback_query
from aiogram.filters import Command
from aiogram import types
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

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

inline4=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Когда дедлайн ЕНТ? ",callback_data="faq1")],
    [InlineKeyboardButton(text="Есть ли гранты? ",callback_data="faq2")],
    [InlineKeyboardButton(text="Иногородние? " , callback_data="faq3")],
    [InlineKeyboardButton(text="Пересдача ЕНТ? ",callback_data="faq4")],
    [InlineKeyboardButton(text="Онлайн-заявка? ",callback_data="faq5")]
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
        await callback.message.answer(
            "Интересные разделы",
                reply_markup=inline2
            )
    elif callback.data=="btn2":
        await callback.message.answer("Бакалавриат — 1,200,000 тг/год (гранты по конкурсу)",reply_markup=inline3)
    elif callback.data=="btn1":
        """📄 Для поступления необходимы:
• Аттестат о среднем образовании  
• Сертификат ЕНТ (минимум 65 баллов)  
• Паспорт или удостоверение личности  
• 6 фотографий 3x4  
• Медицинская справка формы 086-У  
• Дипломы и сертификаты (олимпиады, курсы — для льгот)
        """,

    elif callback.data=="yes" or callback.data=="no":
        await callback.message.answer("Конец")
    elif callback.data=="btn3":
        await callback.message.answer("Часто задаваемые вопросы:",
        reply_markup=inline4)
    elif callback.data=="faq1":
        await callback.message.answer("20 июня — результаты")
    elif callback.data=="faq2":
        await callback.message.answer("Да, конкурс на 30% мест")
    elif callback.data=="faq3":
        await callback.message.answer("Общага при приоритете")
    elif callback.data=="faq4":
        await callback.message.answer("Через 1 месяц")
    elif callback.data=="faq5":
        await callback.message.answer("Да, через egov.kz портал")
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
    

