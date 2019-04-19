__author__ = ' Пономарев Федор Анатольевич'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - копирование указанного файла")
    print("rm <file_name> - удаление указанного файла")
    print("cd <путь> - смена директории")
    print("ls  - Вывод полного пути местонахождения")



def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла для копирования")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        shutil.copy(dir_path, dir_path + '.dupl')
        print('Файл {} скопирован'.format(dir_name))
    except FileExistsError:
        print('Файл {} уже существует'.format(dir_name))
def del_file():
    if not dir_name:
        print("Необходимо указать имя файла для удаления")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    print(dir_path)
    answer = input("Вы уверены что хотите удалить этот файл: ? {}(Y/N)")
    if answer == "y":
        try:
            os.remove(dir_path)
            print('Файл {} удален'.format(dir_name))
        except FileNotFoundError:
            print('Файл {} не существует'.format(dir_name))
    else:
        print("Файл {} не удален ".format(dir_name))
def ping():
    print("pong")
def cd_dir():
    if not dir_name:
        print("Необходимо указать путь к директории вторым параметром")
        return
    dir_path = os.path.join(dir_name)
    try:
        os.chdir(dir_path)
        print('Вы перешли в {}'.format(os.getcwd()))
    except FileNotFoundError:
        print('Неправильно указан путь {}'.format(dir_name))
def ls_dir():
    print(os.getcwd())

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": del_file,
    "cd": cd_dir,
    "ls": ls_dir
}


try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")