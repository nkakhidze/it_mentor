import random
import time
from asyncio import timeout


# Реализуйте:
# 1. Функцию линейного поиска
def linear_finder(n: int, listik: list):
    listik = sorted(listik)
    schtchk = 0
    for i in range(len(listik)):
        schtchk += 1
        if n == listik[i]:
            return f"linear_finder: число {n} было в вашем списке на позиции {i} при сортировке списка по возрастанию.\nЧисло было найдено с {schtchk} попытки"

    return f"linear_finder: числа {n} не было в вашем списке"

# 2. Функцию бинарного поиска
def binar_finder(n: int, listik: list):
    listik = sorted(listik)
    schtchk = 0
    left = 0
    right = len(listik) - 1

    while left <= right:
        mid = (left + right) // 2
        # print('это mid', mid,listik[mid])
        schtchk += 1
        if listik[mid] == n:
            return f"binar_finder: число {n} было в вашем списке на позиции {mid} при сортировке списка по возрастанию.\nЧисло было найдено с {schtchk} попытки"
        if listik[mid] > n:
            right = mid - 1
            # print("new right",right)
            # print('при новом right значение', listik[right])
        else:
            left = mid + 1
            # print("new left", left)
            # print('при новом left значение', listik[left])
        # time.sleep(3)
    return f"binar_finder: числа {n} не было в вашем списке"



# 3. Сравните их производительность на отсортированном списке из 1000 элементов
for_linear_listik1000 = [random.randint(1, 999) for _ in range(1000)]
# for_linear_listik1000 = [random.randint(1, 20) for _ in range(11)]
for_binar_listik1000 = for_linear_listik1000.copy()

sorted_low_time_start = time.perf_counter()
print(linear_finder(227, for_linear_listik1000))
sorted_low_time_stop = time.perf_counter()
print("число было найдено за ",(sorted_low_time_stop - sorted_low_time_start)*1000, "милисекунд")

print("_____________________")

sorted_fast_time_start = time.perf_counter()
print(binar_finder(227, for_binar_listik1000))
sorted_fast_time_stop = time.perf_counter()
print("число было найдено за ",(sorted_fast_time_stop - sorted_fast_time_start)*1000, "милисекунд")

print()
print("****** ищем число 777 *******")
print()

sorted_low_time_start = time.perf_counter()
print(linear_finder(777, for_linear_listik1000))
sorted_low_time_stop = time.perf_counter()
print("число было найдено за ",(sorted_low_time_stop - sorted_low_time_start)*1000, "милисекунд")

print("_____________________")

sorted_fast_time_start = time.perf_counter()
print(binar_finder(777, for_binar_listik1000))
sorted_fast_time_stop = time.perf_counter()
print("число было найдено за ",(sorted_fast_time_stop - sorted_fast_time_start)*1000, "милисекунд")

# 4. Объясните, почему бинарный поиск работает быстрее




# a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(binar_finder(4, a))






