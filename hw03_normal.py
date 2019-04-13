# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    array = []
    array.append(1)
    array.append(1)
    i = 1
    while i < m:
        z = array[i]+array[i-1]
        array.append(z)
        i += 1
    return array[n:m]

z = fibonacci(8, 21)
print(z)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    x = len(origin_list)-1
    x1 = len(origin_list)-1
    for i in range(x):
        for j in range(x1):
            if origin_list[j] > origin_list[j+1]:
                origin_list[j], origin_list[j+1] = origin_list[j+1], origin_list[j]
        x1 -= 1
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0, -13, -15, -18, -20]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def filtrum (mask, origin_list):
    result = []
    for itm in origin_list:
        if itm == mask:
            result.append(itm)
    return result

print (filtrum (2, [2, 10, -12, 2.5, 20, -11, 4, 4, 0, -13, -15, -18, -20]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
arrayx = []
arrayy = []
for i in range(4):
    x = int(input("Введите координату x{}".format(i+1)))
    y = int(input("Введите координату y{}".format(i+1)))
    arrayx.append(x)
    arrayy.append(y)
if (arrayx[0]+arrayx[2] == arrayx[1]+arrayx[3]) and (arrayy[0]+arrayy[2] == arrayy[1]+arrayy[3]):
    print("Вы ввели координаты параллелограмма")
else:
    print("Введенные координаты не являются вершинами параллелограмма")




