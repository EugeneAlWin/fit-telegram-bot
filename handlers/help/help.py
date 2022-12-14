from bot import disp
from aiogram import types
from config import DEFAULT_ADMIN


@disp.message_handler(commands=['help'])
async def help(message: types.Message):
    text = ("Вот что умеет этот бот:\n"
            + "-----Для всех-----\n"
            + "/start - приветствие\n"
            + "/help - справка\n"
            + "/cancel - отмена команды\n"
            + "/getgroup - получить полный список группы\n"
            + "/getsub1 - список первой подгруппы\n"
            + "/getsub2 - список второй подгруппы\n"
            + "/getq1 - получить очередь на лабы первой подгруппы\n"
            + "/getq2 - получить очередь на лабы второй подгруппы\n"
            + "/getmind - получить список напоминаний\n"
            + "/getacc - получить список супер-пользователей\n"
            + "/getshiman - получить расписание деканата\n"
            + "/gett - получить расписание занятий (документом)(timetable)\n"
            + "-----Для уполномоченных-----\n"
            + "/setgroup - перезаписать список всей группы (admin)\n"
            + f"/setq - сгенерировать очередь на лабу для подгруппы ({DEFAULT_ADMIN} only)\n"
            + "/setmind - установить напоминание (admin)\n"
            + "/remmind - удалить напоминание (admin)\n"
            + "/setacc @user1 @user2... - дать доступ пользователю (admin). Перечислить пользователей через @\n"
            + "/remacc @user1 @user2...-  убрать доступ пользователя (admin). Перечислить пользователей через @\n"
            + "/setshiman - записать новое расписание деканата (admin)\n"
            + "/sett url - перезаписать ссылку на документ (admin). url - ссылка на pdf.\n"
            + "/maxim - послание для Максима.\n"
            + "/exclude - викторина.\n"
            + "-----P.S.-----\n"
            + "Для многих команд нужны права администратора (для тех, кто не понял).\n" +
            "Ещё этот бот пытается пересылать сообщения из Новостей вк в телеграм. Удобно для тех, кто не хочет часто заходить ВК. "
            + "Но вы иногда проверяйте, чтоб он ничего не пропустил... \n"
            + "Бот не работает? Пишите сюда: https://github.com/EugeneAlWin/fit-telegram-bot/issues")
    await message.answer(text)
