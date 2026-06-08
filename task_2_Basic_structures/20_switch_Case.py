# Дано целое число K. Вывести строку-описание оценки, соответствующей числу
# K(1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»).
# Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».

listik = (1, 2, 3, 4, 5, 6, -4, "Привет", (3,), 4.3, 4.5, True, None)


def get_text_describing_assessment(n):
    match n:
        case 1:
            print("плохо")
        case 2:
            print("неудовлетворительно")
        case 3:
            print("удовлетворительно")
        case 4:
            print("хорошо")
        case 5:
            print("отлично")
        case _:
            print("ошибка")



# for l in listik:
#     print(l, end=" — ")
#     get_text_describing_assessment(l)

import math
import time
import logging

logging.basicConfig(level=logging.DEBUG, filename="py_log_2.20.log",filemode="w")
# logging.basicConfig(level=logging.DEBUG)

def math_round(n):
    return math.floor(n + 0.5) if n > 0 else math.ceil(n - 0.5)


for l in listik:
    # time.sleep(1)
    try:
        l_round = math_round(l)
        print(l, end=" — ")
        get_text_describing_assessment(l_round)
    # except Exception as e:
    except Exception as e:
        logging.error("Ошибка: %s. Вместо числа было передано %s: '%s'", e, type(l), l)


