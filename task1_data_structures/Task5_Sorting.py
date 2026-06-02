import random, time


# Реализуйте:
# 1. Пузырьковую сортировку
def sort_bubbling(massiv:list):
    for iteraczia in range(len(massiv)-1):
        schtchk = 0
        for i in range(len(massiv) - 1 - iteraczia):
            if massiv[i] > massiv[i + 1]:
                massiv[i], massiv[i + 1] = massiv[i + 1], massiv[i]
                schtchk += 1
            i+= 1
        if schtchk == 0:
            return massiv
    return massiv



# 2. Сортировку вставками
def sort_pasting(massiv:list):
    for i in range(1, len(massiv)):
        while (massiv[i] < massiv[i - 1]) and (i > 0):
            massiv[i - 1], massiv[i] = massiv[i], massiv[i - 1]
            i -= 1
    return massiv





# 3. Сравните их с встроенной функцией sorted()
if __name__ == "__main__":
    a = [1, 0, 24, 2, 5, 0, 12]
    b, c, d = a.copy(), a.copy(), a.copy()
    b = sort_bubbling(b)
    c = sort_pasting(c)
    d = sorted(d)
    print(a)
    print(b)
    print(c)
    print(d)

    print(b == c == d)

# 4. Измерьте время выполнения для разных размеров входных данных

def fill_list(n):
    return [random.randint(-500, 500) for _ in range(n)]

if __name__ == "__main__":
    a = fill_list(10)
    b, c, d = a.copy(), a.copy(), a.copy()


    sort_bubbling_time_start = time.perf_counter()
    b = sort_bubbling(b)
    sort_bubbling_time_stop = time.perf_counter()
    print("Пузырёк, 10 эл-в —", (sort_bubbling_time_stop - sort_bubbling_time_start) * 1000, "мс")

    sort_pasting_time_start = time.perf_counter()
    c = sort_pasting(c)
    sort_pasting_time_stop = time.perf_counter()
    print("Вставки, 10 эл-в — ", (sort_pasting_time_stop - sort_pasting_time_start) * 1000, "мс")

    sorted_time_start = time.perf_counter()
    d = sorted(d)
    sorted_time_stop = time.perf_counter()
    print("sorted, 10 эл-в — ", (sorted_time_stop - sorted_time_start) * 1000, "мс")

    print("_________________________")

    a = fill_list(100)
    b, c, d = a.copy(), a.copy(), a.copy()


    sort_bubbling_time_start = time.perf_counter()
    b = sort_bubbling(b)
    sort_bubbling_time_stop = time.perf_counter()
    print("Пузырёк, 100 эл-в —", (sort_bubbling_time_stop - sort_bubbling_time_start) * 1000, "мс")

    sort_pasting_time_start = time.perf_counter()
    c = sort_pasting(c)
    sort_pasting_time_stop = time.perf_counter()
    print("Вставки, 100 эл-в — ", (sort_pasting_time_stop - sort_pasting_time_start) * 1000, "мс")

    sorted_time_start = time.perf_counter()
    d = sorted(d)
    sorted_time_stop = time.perf_counter()
    print("sorted, 100 эл-в — ", (sorted_time_stop - sorted_time_start) * 1000, "мс")

    print("_________________________")

    a = fill_list(5000)
    b, c, d = a.copy(), a.copy(), a.copy()


    sort_bubbling_time_start = time.perf_counter()
    b = sort_bubbling(b)
    sort_bubbling_time_stop = time.perf_counter()
    print("Пузырёк, 5000 эл-в —", (sort_bubbling_time_stop - sort_bubbling_time_start) * 1000, "мс")

    sort_pasting_time_start = time.perf_counter()
    c = sort_pasting(c)
    sort_pasting_time_stop = time.perf_counter()
    print("Вставки, 5000 эл-в — ", (sort_pasting_time_stop - sort_pasting_time_start) * 1000, "мс")

    sorted_time_start = time.perf_counter()
    d = sorted(d)
    sorted_time_stop = time.perf_counter()
    print("sorted, 5000 эл-в — ", (sorted_time_stop - sorted_time_start) * 1000, "мс")

    print("_________________________")