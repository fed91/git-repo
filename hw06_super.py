__author__ = ' Пономарев Федор Анатольевич'

human_data = ['BIll Jobs 22 Red Russia Moscow Male',
             'Steve Jobs 28 White Russia Moscow Male',
             'John Jobs 19 Black Russia St-Petersburg Male',
              'Иван Иванов 23 Белый Россия Новосибирск Муж',
              'Tim Cook 25 White Russia Moscow, male']

import re

class FileDB:
    filename = str()
    __file = None
    __columns = (
        'id',
        'name',
        'surname',
        'age',
        'color',
        'country',
        'city',
        'sex',
    )

    def __init__(self, filename):
        self.filename = filename
        header = '|' + f"|".join(self.__columns) + '|'
        self.__create_header(header)

    def __open_session(self, param):
        self.__file = open(self.filename, param, encoding='UTF-8')

    def __close_session(self):
        self.__file.close()

    def __create_header(self, data):
        self.__open_session('w')
        self.__file.write(data + '\n')
        self.__close_session()

    def read_data(self):
        self.__open_session('r')
        data = self.__file.read()
        self.__close_session()
        return data
    def find_data(self,mask):
        self.__open_session('r')
        find_db=[]
        _idd = len (self.__file.readlines())
        self.__file.seek(0)
        for i in range(_idd):
            data = self.__file.readline()
            result = re.findall(mask, data)
            if result:
                find_db.append(human_db[i-1])
        self.__close_session()
        return find_db
    def add_data(self, data):
        self.__open_session('r+')
        _idd = len (self.__file.readlines())
        self.__file.write('|'+str(_idd) + data.to_db() + '\n')
        self.__close_session()


class Human:
    name = str()
    surname = str()
    age = int()
    color = str()
    country = str()
    city = str()
    sex = str()

    def __init__(self, human_data):
        human_data = human_data.split(" ")
        self.name = human_data[0]
        self.surname = human_data[1]
        self.age = human_data[2]
        self.color = human_data[3]
        self.country = human_data[4]
        self.city = human_data[5]
        self.sex = human_data[6]

    def to_db(self):
        data = f'|{self.name}|{self.surname}|{self.age}|{self.color}|{self.country}|{self.city}|{self.sex}|'
        return data


database = FileDB('testdb')
human_db = []
for itm in human_data:
    human_db.append(Human(itm))

#human_db.append(Human(human_data[1]))
#human_db.append(Human(human_data[2]))
for h in human_db:
    database.add_data(h)

for h in human_db:
    print(h.to_db())
a= database.find_data(input("Введите фильтр для поиска:"))
print(a)
for h in a:
    print(h.to_db())

