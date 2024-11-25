class Bachelor():
    def __init__(self, firstName, lastName, group, averageMark):
        if isinstance(firstName, str) and isinstance(lastName, str) and isinstance(group, int) and isinstance(averageMark, (int, float)):
            self._firstName = firstName
            self._lastName = lastName
            if group >= 0: self._group = group
            else: raise ValueError('Номер группы не может быть отрицательным')
            if averageMark >= 0: self._averageMark = averageMark
            else: raise ValueError('Средняя оценка не может быть отрицательной')
        else: return NotImplemented

# Если средняя оценка студента равна 5, то сумма 10000 р, иначе, если средняя оценка больше 3, то 5000, иначе - 0.
    def getScholarship(self):
        if self._averageMark == 5: return 10000
        elif 3 < self._averageMark < 5: return 5000
        else: return 0

class Undergraduate(Bachelor):
    def __init__(self, firstName, lastName, group, averageMark):
        Bachelor.__init__(self, firstName, lastName, group, averageMark)

# Если средняя оценка магистранта равна 5, то сумма 15000 р, иначе, если средняя оценка больше 3, то 7500 р, иначе - 0.
    def getScholarship(self):
        if self._averageMark == 5: return 15000
        elif 3 < self._averageMark < 5: return 7500
        else: return 0

students = [Bachelor('Саша', 'Шеметов', 14123, 4), Bachelor('Семён', 'Ильин', 14123, 4.5), Undergraduate('Никита', 'Степанов', 13121, 4.8), Undergraduate('Никита', 'Долбак', 10121, 5), Bachelor('Артём', 'Шишкин', 14121, 0)]
for student in students:
    print(student.getScholarship())

