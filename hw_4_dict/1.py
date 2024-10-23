# Вариант 5
"""
test data:
4
Завод_А 1000 950
Фабрика_Б 1500 1650
Комбинат_В 1200 1200
Склад_Г 800 700
"""

n = int(input('Введите кол-во предприятий: '))
print('Введите информацию о предприятиях построчно в виде: Название_преприятия Плановый_объем_р_т Фактический_объем_р_т:')
data = {key: [int(v1), int(v2)] for key, v1, v2 in (input().split() for _ in range(n))}
print('')

percentage_of_plan_completion = {key: value[1] * 100 / value[0]  for key, value in data.items()}

c = 0
for value in percentage_of_plan_completion.values(): 
    if value <= 90: c += 1

for key, value in percentage_of_plan_completion.items():
    print(f'{key} : процент выполнения плана {value}')
print(f'Количество предприятий, недовыполнивших план на 10% и более: {c}')