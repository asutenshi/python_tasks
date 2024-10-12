n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]
black_dots = {}

for i, line in enumerate(data):
    dots_in_line = []
    for j, char_ in enumerate(line):
        if char_ == '*': dots_in_line.append(j)
    if dots_in_line:
        black_dots[i] = dots_in_line
# пример data : [['.', '*', '.'], ['.', '*', '.'], ['.', '*', '.'], ['.', '*', '.']]
# пример black_dots : {0: [1], 1: [1], 2: [1], 3: [1]} {строка : [индексы симоволов с *]}

upper_bound = min(black_dots)
lower_bound = max(black_dots)
left_bound = min(min(v) for v in black_dots.values())
rigth_bound = max(max(v) for v in black_dots.values())

for i in range(upper_bound, lower_bound+1):
    for j in range(left_bound, rigth_bound+1):
        if data[i][j] == '.': data[i][j] = '*'

# print для разделения входных данных и ответа при выводе
print()
for line in data:
    print(''.join(line))