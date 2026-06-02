import sys
from Task5_Sorting import fill_list

# Задание 6: Работа с памятью
# Напишите программу, которая:
# 1. Создает список и кортеж одинакового размера
n = 10
listik = fill_list(n)
tuplik = tuple(listik)

print(listik)
print(tuplik)

# 2. Измеряет объем памяти, занимаемый каждым
print(f"кортеж из {n} элементов занимает {sys.getsizeof(tuplik)} байт")
print(f"список из {n} элементов занимает {sys.getsizeof(listik)} байт")

# 3. Демонстрирует, как изменяется размер списка при добавлении элементов
print("______________")
listik.append(2)
print(f"добавили int(2) — занимает {sys.getsizeof(listik)} байт")

# listik.extend((2,2,2,2,2))
listik.extend((2,2,2,2,2,2))
print(listik)
print(f"добавили 5/6 int(2) — занимает {sys.getsizeof(listik)} байт")