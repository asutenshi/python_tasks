from functools import singledispatchmethod
from datetime import date, datetime


class BirthInfo():
    @singledispatchmethod
    def __init__(self, arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    # Можно было не реализовывать проверку на корректность даты, т.к. datetime.date это учитывает, но у меня была написана эта проверка в другом задании
    # почему бы и не переиспользовать)

    def __check_date(self, arg):
        _m_31 = (1, 3, 5, 7, 8, 10, 12)
        _m_30 = (4, 6, 9, 11)
        if len(arg) == 3:
            year = arg[0]
            month = arg[1]
            day = arg[2]
            if year < 0: raise ValueError('Год не может быть отрицательным числом')
            if 12 < month < 1: raise ValueError('Месяц не может быть меньше 1 или числом большим 12')
            if 31 < day < 1: raise ValueError('День не может быть меньше 1 или числом большим 31')
            else: 
                if month in _m_31 and day > 31: raise ValueError('Такой даты не существует')
                elif month in _m_30 and day > 30: raise ValueError('Такой даты не существует')
                else:
                    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                        if day > 29: raise ValueError('Такой даты не существует')
                    else:
                        if day > 28: raise ValueError('Такой даты не существует')
        else: raise ValueError('Неправильно введена дата')
        return True

    @__init__.register(date)
    def _(self, arg):
        self._birth_date = arg;

    @__init__.register(str)
    def _(self, arg):
        temp = list(map(int, arg.split('-')))
        if (self.__check_date(temp)):
            self._birth_date = date(temp[0], temp[1], temp[2])


    @__init__.register(list | tuple)
    def _(self, arg):
        if(self.__check_date(arg)):
            self._birth_date = date(arg[0], arg[1], arg[2])

    @property
    def age(self):
        self.__age = date.today().year - self._birth_date.year
        if (date.today().month, date.today().day) < (self._birth_date.month, self._birth_date.day):
            self.__age -= 1
        return self.__age

def current_age(birth_date):
    if isinstance(birth_date, date):
        age = date.today().year - birth_date.year
        if (date.today().month, date.today().day) < (birth_date.month, birth_date.day):
            age -= 1
        return age
    else: return NotImplemented

d1 = BirthInfo('2005-12-15')
d2 = BirthInfo(date(1992, 11, 12))
d3 = BirthInfo([2077, 12, 12])

for bd in (d1, d2, d3):
    for d in (date(2005, 12, 15), date(1992, 11, 12), date(2077, 12, 12)):
        if current_age(d) == bd.age:
            print('Yes, age was посчитан correctly')
