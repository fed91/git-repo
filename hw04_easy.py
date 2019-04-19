__author__ = ' Пономарев Федор Анатольевич'

# Все задачи текущего блока решите с помощью генераторов списков!
import random
# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

def get_spisok(num, n, m):
    array = []
    for _ in range(num):
        array.append(random.randint(n, m))
    return array
spisok = get_spisok(10, 0, 20)
spisok2 = list(map(lambda x: x**2, spisok))
print(spisok)
print(spisok2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruit1 = ["яблоко", "банан", "киви", "арбуз", "виноград","яблоко", "арбуз"]
fruit2 = ["яблоко", "киви", "арбуз", "Дыня", "Апельсин"]
result = []
fruit1 = set(fruit1)
fruit2 = set(fruit2)
for fr1 in fruit1:
    for fr2 in fruit2:
        if fr1 == fr2:
            result.append(fr1)
print(result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

spisok = get_spisok(10, -10, 20)
spisok2 = []
for _ in spisok:
    if not _%3 and _>0 and _%4:
        spisok2.append(_)
print(spisok)
print(spisok2)
