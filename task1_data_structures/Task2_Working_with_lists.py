# Задание 2: Работа со списками.
# Создайте программу, которая:
# 1. Создает список из 10 чисел
import random
import time


def rand_10x():
    a = []
    for i in range(10):
        a.append(random.randint(0,100))
    return a

a = rand_10x()
b = a.copy()

# 2. Находит максимальное и минимальное значение
a_min = min(a)
a_max = max(a)

# 3. Сортирует список двумя разными способами
sorted_fast_time_start = time.perf_counter()
# print(sorted_fast_time_start)
a_sorted_fast = sorted(a)
sorted_fast_time_stop = time.perf_counter()
# print(sorted_fast_time_stop)
time_sorted = (sorted_fast_time_stop - sorted_fast_time_start) * 1000
print("для функции 'sorted' время сортировки:", time_sorted)


sorted_low_time_start = time.perf_counter()
for i in range(0, len(b)):
    # print('i =', b[i])
    for j in range(i+1, len(b)):
        # print('j =', b[j],"*")
        if b[i] > b[j]:
            b[i], b[j] = b[j], b[i]
        # print('j =', b[j], end=' ')
    # print()
sorted_low_time_stop = time.perf_counter()
print(b)
time_puzirek = (sorted_low_time_stop - sorted_low_time_start) * 1000
print("для функции 'типа пузырёк' время сортировки:", time_puzirek)

# 4. Измеряет время выполнения каждой операции сортировки

print(f"функция 'sorted' отрабатывает быстрее функции 'типа пузырёк' для списка длиной {len(a)} в {time_sorted / time_puzirek} раз")