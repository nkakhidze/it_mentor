# Написать программу на Python
# для решения квадратного уравнения ax^2 + bx + c = 0.
# Если дискриминант отрицателен,
# программа должна выдать ошибку и предложить пользователю попробовать еще раз с другими коэффициентами.
# При выполнении скрипта в лог должна записываться информация о успехе или неудаче операции.
import logging

logging.basicConfig(level=logging.INFO, filename="py_log_2.16.log",filemode="w")

def solve_quadratic_equation(a, b, c) -> tuple:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        logging.info(f"Не успех. Дискриминант < 0 => нет решения уравнения при {a}, {b}, {c}")
        return (False,)
    elif discriminant == 0:
        logging.info("Успех. Дискриминант = 0 => уравнение имеет одно решение.")
        return (-b / 2*a,)
    else:
        logging.info("Успех. Дискриминант > 0 => уравнение имеет 2 решения.")
        return ((-b + (discriminant)**(1/2)) / (2*a),
                (-b - (discriminant)**(1/2)) / (2*a),
                )

# print(solve_quadratic_equation(1,-2,3))
# print(solve_quadratic_equation(1,5,5))
# print(solve_quadratic_equation(1,-5,1))

while True:
    try:
        a, b, c = map(float, input().split())
        solution = solve_quadratic_equation(a, b, c)
        if solution[0] != False:
            print("Ваш ответ:", solution)
            break
        else:
            print("попробуйте еще раз с другими коэффициентами")
    except ValueError:
        print("Для решения квадратного уравнения требуется ввести коэффициенты через знак пробела, например, '1, 5, 5'")
