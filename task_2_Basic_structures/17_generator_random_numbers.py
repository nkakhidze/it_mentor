# Написать программу для генерации случайных чисел в заданном диапазоне.
# Если пользователь ввел недопустимые границы диапазона (например, меньше нуля),
# программа должна вывести ошибку и попросить ввести диапазон заново.
# Информация об ошибках должна быть записана в лог.

import logging
import random


class ErrorNegativeCount(ValueError):
    pass
class ErrorSequenceBoundary(ValueError):
    pass


logging.basicConfig(level=logging.INFO, filename="py_log_2.17.log",filemode="w")

def get_random_number_generator(n, a, b):
    if n < 0:
        raise ErrorNegativeCount("Количество чисел не может быть отрицательным")
    if a > b:
        raise ErrorSequenceBoundary("нижняя граница последовательности не может быть больше верхней")
    return [random.randint(a, b) for _ in range(n)]

# print(get_random_number_generator(-5, 6, 9))

if __name__ == '__main__':
    while True:
        try:
            user_input = input(
                "Введите строкой через пробел: "
                "(1) сколько случайных чисел вывести "
                "(2) минимальное "
                "(3) максимальное значение в последовательсности \n"
            )
            n, a, b = map(int, user_input.split())
            print(get_random_number_generator(n, a, b))

            break

        except ErrorNegativeCount as error:
            logging.error("Ошибка: %s. Были введены: %s", error, user_input)
            print("Ошибка: количество чисел не может быть отрицательным. Попробуйте ещё раз.")
        except ErrorSequenceBoundary as error:
            logging.error("Ошибка: %s. Были введены: %s", error, user_input)
            print("Ошибка: нижняя граница последовательности не может быть больше верхней")
        except ValueError as error :
            logging.error("Ошибка: %s. Пользователь ввёл данные в неверном формате: %s", error, user_input)
            print("Ошибка: введите ровно 3 числа по типу '5 7 100'")
        except Exception as error:
            logging.error("Ошибка: %s. Были введены: %s", error, user_input)
            print("Непредвиденная ошибка: введите, пожалуйста, числа по типу '5 7 100'")


