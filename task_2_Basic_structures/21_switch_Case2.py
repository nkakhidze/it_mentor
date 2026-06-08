# Даны два целых числа: D(день) и M (месяц),
# определяющие правильную дату невисокосного года.
# Вывести значения D и M для даты, следующей за указанной.


# import datetime
#
# d = 4
# m = 4
# date_str = datetime.date(day=d, month=m, year=2020)
# print(date_str)
# print(datetime.datetime.strptime(str(date_str), '%Y-%m-%d'))



from datetime import datetime, timedelta

d, m = int(input("Введите день ")), int(input("Введите месяц "))

months = (
    "", "января", "февраля", "марта", "апреля", "мая", "июня",
    "июля", "августа", "сентября", "октября", "ноября", "декабря"
)

date_str = f'2026-{m}-{d}'

date_obj = datetime.strptime(date_str, '%Y-%m-%d')
next_day_obj = date_obj + timedelta(days=1)
# Получаем день, год и название месяца по его номеру
day = next_day_obj.day
month_name = months[next_day_obj.month]
year = next_day_obj.year

# Собираем красивую строку (без ведущих нулей)
formatted_date = f"{day} {month_name} {year} года"

print("Завтра будет.....", formatted_date)  # Выведет: 4 апреля 2020 года