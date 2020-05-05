import datetime

age = int(input("Введите ваш год рождения: "))
now_time = datetime.date.today()
year = int(now_time.year)


def calculate_age( age, year ):
    return year - age


total = year - age
print("Ваш возраст " + str(total))
