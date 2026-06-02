# # Вывести все числа от 1 до 100, которые делятся на 3 без остатка.
# for num in range(1, 100):
#     if num % 3 == 0:
#         print(num)

# # Найти все простые числа от 2 до 50.
# easy_numbers = []
# for num in range(2, 50):
#     flag = True
#     for num2 in range(2, num-1):
#         if num % num2 == 0:
#             flag = False
#             break
#     if flag:
#         easy_numbers.append(num)
#
# print(easy_numbers)

# Посчитать сумму квадратов чисел от 1 до 10.
# print(sum(i**2 for i in range(1, 11)))


# # Вывести значения функции y=x^2 от 1 до 10 с шагом 0.5.
# for i in range(1, 10):
#     print(i**2)
#     print((i+0.5)**2)


# Напишите рекурсивную функцию, которая находит факториалы чисел от 1 до 5 (включительно).
def func(n):
    if n == 1:
        return 1
    return n * func(n - 1)

print(func(3))