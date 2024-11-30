class USADate():
    _m_31 = (1, 3, 5, 7, 8, 10, 12)
    _m_30 = (4, 6, 9, 11)
    def __init__(self, year, month, day):
        if isinstance(year, int) and isinstance(month, int) and isinstance(day, int):
            if year >= 0: self._year = year
            else: raise ValueError('Год не может быть отрицательным числом')
            if 1 <= month <= 12: self._month = month
            else: raise ValueError('Месяц не может быть меньше 1 или числом большим 12')
            if 1 <= day <= 31: 
                if month in self._m_31 and day <= 31:
                    self._day = day
                elif month in self._m_30 and day <= 30:
                    self._day = day
                else:
                    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                        if day <= 29: self._day = day
                        else: raise ValueError('Такой даты не существует')
                    else:
                        if day <= 28: self._day = day
                        else: raise ValueError('Такой даты не существует')
            else: raise ValueError('День не может быть меньше 1 или числом большим 31')
        else: return NotImplemented

    def format(self):
        return f'{self._month:02d}-{self._day:02d}-{self._year:04d}'

    def iso_format(self):
        return f'{self._year:04d}-{self._month:02d}-{self._day:02d}'

class ItalianDate(USADate):
    def __init__(self, year, month, day):
        USADate.__init__(self, year, month, day)

    def format(self):
        return f'{self._day:02d}/{self._month:02d}/{self._year:04d}'

date = list(map(int, input('Введите дату в формате (year=int month=int day=int):').split()))

u = USADate(date[0], date[1], date[2])
i = ItalianDate(date[0], date[1], date[2])

for d in (u, i):
    print(f'{d.__class__.__name__}: format: {d.format()}, iso_format: {d.iso_format()}')
