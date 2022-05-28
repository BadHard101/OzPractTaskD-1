"""
Необходимо создать текстовый файл и реализовать функцию логирования (без использования модуля
logging). Функция должна вызываться из каждого метода ранее реализованных классов и записывать в
файл строки следующего содержания: КЛЮЧ --- ДАТА И ВРЕМЯ --- КОММЕНТАРИЙ.
Ключи: CRE (создание экземпляра класса), INF (изменение), ERR (сработало исключение).
Комментарий: создано …, удален …, добавлен …, распечатан …
"""
from datetime import datetime



def log(key, obj="undef_obj", func="undef_func", inf="undef_inf"):
    f = open("log.txt", "a", encoding="utf-8")
    if key == "CRE":
        f.write(key + "---" + datetime.now().strftime("%d/%m/%Y/%H:%M:%S") + "---" + f"{obj} was created by {func}.\n")
    elif key == "INF":
        if inf == "del":
            f.write(key + "---" + datetime.now().strftime("%d/%m/%Y/%H:%M:%S") + "---" + f"{obj} was deleted by {func}.\n")
        elif inf == "add":
            f.write(key + "---" + datetime.now().strftime("%d/%m/%Y/%H:%M:%S") + "---" + f"{obj} was added by {func}.\n")
        elif inf == "prt":
            f.write(key + "---" + datetime.now().strftime("%d/%m/%Y/%H:%M:%S") + "---" + f"{obj} was printed by {func}.\n")
        elif inf == "chg":
            f.write(key + "---" + datetime.now().strftime("%d/%m/%Y/%H:%M:%S") + "---" + f"{obj} was changed by {func}.\n")
    elif key == "ERR":
        f.write(key + "---" + datetime.now().strftime("%d/%m/%Y/%H:%M:%S") + "---" + f"{obj} caused by {func}.\n")
    f.close()