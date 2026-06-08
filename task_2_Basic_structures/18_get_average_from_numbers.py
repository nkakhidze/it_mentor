# Написать программу для нахождения среднего арифметического списка чисел.
# Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка),
# программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.
# Информация об ошибках должна быть записана в лог.
import logging

class NotListError(TypeError):
    pass


class NotNumberError(Exception):
    pass

logging.basicConfig(level=logging.INFO, filename="py_log_2.16.log",filemode="w")
# logging.basicConfig(level=logging.INFO)


def get_average_from_numbers(input_numbers: list):
    if type(input_numbers) is not list:
        raise NotListError("Передали не List")
    if len(input_numbers) == 0:
        raise ValueError("Список не должен быть пустым")
    summa = 0
    for number in input_numbers:
        if not isinstance(number, (int, float)):
            raise NotNumberError("В списке были не только цифры")
        summa += number
    return summa / len(input_numbers)



a1 = [10, 20, 30, 40, 50]   # Проверка базовой работоспособности.

a4 = [1.5, 2.5, 3.75, 4.25] # Проверка работы с типом float.

a3 = []                     # Проверка обработки деления на ноль (ZeroDivisionError).

a2 = "10, 20, 30"           # Проверка обработки TypeError (ввод не является итерируемым объектом нужного типа).

a5 = [10, "20", 30]         # Проверка обработки ошибки типов внутри итерации (TypeError при попытке сложения).

a6 = [10, None, 30]         # Проверка устойчивости к отсутствующим значениям.

a7 =  42                    # Проверка обработки ошибки, когда объект не является итерируемым.

listiki = [a1, a2, a3, a4, a5, a6, a7]

for listik in listiki:
    try:
        print(listik)
        print(get_average_from_numbers(listik))
    except NotListError as e:
        logging.error("Ошибка: %s. Входные данные: %s",e, listik)
    except ValueError as e:
        logging.error("Ошибка: %s. Входные данные: %s",e, listik)
    except NotNumberError as e:
        logging.error("Ошибка: %s. Входные данные: %s", e, listik)
    except Exception as e:
        logging.error("Ошибка: %s. Входные данные: %s",e, listik)
