input = []
output = {}

with open('roles.txt', 'r', encoding='utf-8') as file:
    for line in file:
        input.append(line.replace('\n', ''))

for _, item in enumerate(input):
    item = item.strip()
    if item == 'roles:':
        continue
    if item == 'textLines:':
        break
    output[item] = []

for i, line in enumerate(input):
    if line == 'textLines:':
        input = input[i+1:]

role = ''
# for i, line in enumerate(input):
#     temp_role = line.split(':')[0]
#     if temp_role in output and line[0] != ' ':
#         temp_line = line.split(':')[1].strip()
#         if temp_line != '':
#             output[temp_role].append(f'{i+1}) {temp_line}')
#             role = temp_role
#         else: 
#             role = temp_role
#             continue
#     else:
#         output[role].append(f'{i+1}) {line.strip()}')

c_role = 1
for i, line in enumerate(input):
    temp = line.split(':')
    if len(temp) == 1 and temp[0] in output:
        c_role +=1
        continue
    print(line)
    if temp[1] == '    ':
        c_role += 1
        continue
    if line[0] == ' ':
        output[temp[0]] += f'; {line.stip()}'
    output[temp[0]].append(f'{c_role}) ' + ''.join(temp[1:]))
    c_role += 1

for role, lines in output.items():
    print(role + ':')
    for line in lines:
        print(line)
