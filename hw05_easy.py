__author__ = ' Пономарев Федор Анатольевич'

import sys
import shutil
import os
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(path)
    except FileExistsError:
        return "Папка {} уже существует!".format(path)
    return "Создана папка: {}".format(path)
def del_dir(dir_name):
    path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(path)
    except FileNotFoundError:
        return "Директории с именем {} не существует!".format(path)
    return "Удалена папка: {}".format(path)
if __name__ == "__main__":
    action = input("1 - для создания папки, 2 - для удаления, другая - для выхода")
    if action == "1":
        name = input("Введите название директории для создания:")
        for i in range(5):
            name = name + str(i)
            print(make_dir(name), name)
            name = name[:-1]
    elif action == "2":
        name = input("Введите название директории для удаления:")
        for i in range(5):
            name = name + str(i)
            print(del_dir(name), name)
            name = name[:-1]

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_dirs():
    for i in os.listdir():
        if os.path.isdir(str(i)): print(i)
if __name__ == "__main__":
    print("Текущие папки:")
    show_dirs()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
if __name__ == "__main__":
    name = sys.argv
    shutil.copy(name[0], name[0] + '.dupl')
