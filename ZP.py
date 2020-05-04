from typing import List

name1 = input("Зарплата 1 сотрудника: ")
name2 = input("Зарплата 2 сотрудника: ")
name3 = input("Зарплата 3 сотрудника: ")
name1 = int(name1)
name2 = int(name2)
name3 = int(name3)
staff = [name1, name2, name3]


def zp(stuff):
    return sum(stuff) / len(stuff)


a = sum(staff) / len(staff)
a = int(a)
print("Средняя зарплата "+ str(a))
