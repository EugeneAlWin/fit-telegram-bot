import random
from bot import disp
from aiogram import types


@disp.message_handler(commands=["maxim"])
async def shiman_worktime(message: types.Message):
    list_of_max =[
        "иди нахуй",
        "гомосек",
        "отчислен",
        "петух",
        "норм чел",
        "покоритель негроw",
        "любит негроw",
        "ебет негроw",
        "ненавидит негроw",
        "любит сосать у негроw",
        "затащил",
        "построит бассейн"
    ]
    range_of_num = list(range(1, len(list_of_max) + 1))
    random.shuffle(range_of_num)
    await message.answer("Максим Матарас "+list_of_max[0])
