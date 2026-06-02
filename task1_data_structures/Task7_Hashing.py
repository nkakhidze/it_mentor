# import
# Создайте программу, которая:
# 1. Демонстрирует работу хэш-функции для разных типов данных

hashable_listik=[0, "2", 7.8, (5, 6), None, True, False]
unhashable_listik=[[2, 3], (5, [2, 3]), {"key": "value"}, {2, 3, 4}]

def show_hash(listik: list):
    for item in listik:
        try:
            print(f"для объекта {item} типа {type(item)} hash = {hash(item)}")
        except TypeError:
            print(f"для объекта {item} типа {type(item)} отсутсвует hash")

print(show_hash(hashable_listik))
print("_________")
print(show_hash(unhashable_listik))

# 2. Показывает, почему некоторые типы данных нельзя использовать как ключи словаря


# 3. Объясняет, что такое коллизии и как они обрабатываются