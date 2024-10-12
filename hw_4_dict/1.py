# data = {'Предприятие А': [100000, 80000], 'Предприятие Б': [80000, 90000], 'Предприятие В': [120000, 62000]}
print('Введите кол-во предприятий: ')
n = int(input())
print('Введите информацию о предприятиях построчно в виде: Название_преприятия Плановый_объем_р_т Фактический_объем_р_т')
print(input().split())
data = {key : [int(v1), int(v2)] for key, v1, v2 in tuple(input().split()) for _ in range(n)}

percentage_of_plan_completion = {key: data[key][1] * 100 / data[key][0]  for key in data}
c = 0
for value in percentage_of_plan_completion.values(): 
    if value <= 90: c += 1
print(percentage_of_plan_completion, c)