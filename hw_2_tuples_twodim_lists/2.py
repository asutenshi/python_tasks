data = [[list(map(int, input().split())) for _ in range(list(map(int, input().split()))[0])] for _ in range(int(input()))]
check = 1

# алгоритм основывается на сравнении чисел по квадрату по часовой стрелке
for _, table in enumerate(data):
    for i, (current_line, next_line) in enumerate(zip(table, table[1:])):
        for j, (current_number, next_number) in enumerate(zip(current_line, current_line[1:])):
            if current_number == next_number:
                if next_line[j+1] == next_number:
                    if next_line[j+1] == next_line[j]:
                        check = 0
                        break
    if check == 0: print('NO')
    else: print('YES')