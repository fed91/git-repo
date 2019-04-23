# This Python file uses the following encoding: utf-8
__author__ = ' Пономарев Федор Анатольевич'

class Worker:
    name = str()
    surname = str()
    zp = int()
    place = str()
    norma = int()
    otrab = int()
    poluchka = int()

    def __init__(self, worker_data):
        worker_data = str(worker_data).strip()
        worker_data = worker_data.split(" ")
        self.name = worker_data[0]
        self.surname = worker_data[1]
        self.zp = worker_data[2]
        self.place = worker_data[3]
        self.norma = worker_data[4]

    def print_data(self):
        data = f'|{self.name}|{self.surname}|{self.zp}|{self.place}|{self.norma}|{self.otrab}|{self.poluchka}|'
        return data


def prepare_data(data):
    data1 = []
    for i in data:
        a=""
        i = i.strip()
        i = i.split(" ")
        for itm in i:
            if itm != '':
                a = a + " " + str(itm)
        data1.append(a)
    return data1


f = open("workers.txt", "r", encoding="UTF-8")
f2 = open("hours_of.txt", "r", encoding="UTF-8")
vedomost = prepare_data(f.readlines())
vedomost2 = prepare_data(f2.readlines())
f.close()
f2.close()
ved = []
workers = []
for i in range(len(vedomost)):
    workers.append(Worker(vedomost[i]))
for i in vedomost2:
    ved = i.split(" ")
    for x in range(len(workers)):
        if ved[1]== workers[x].name and ved[2] == workers[x].surname:
            workers[x].otrab = ved[3]
x=1
while x < len(workers):
    a = int(workers[x].norma)
    b = int(workers[x].otrab)
    c = int(workers[x].zp)
    if a > b :
        workers[x].poluchka = round(c/a *b, 2)
    else:
        workers[x].poluchka = round((c + (c/a*2*(b-a))),2)
    x += 1
workers[0].poluchka = 'К получению'
for i in range(len(workers)):
    print(workers[i].print_data())

