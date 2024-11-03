# Task 7

import re


def make_buffer_list(number, role, phrase):
    mbl = [number, role, phrase.strip(role)]
    return mbl

with open('roles.txt', 'r', encoding='utf-8') as file:
    # creating roles list
    a = "\n"
    roles = [f'{file.readline().strip(a)}:' for _ in range(26)]
    roles.pop(0)
    # db - dict with roles-keys and phrases-values
    db = {_: [] for _ in roles}
    # regular expression for easier roles sorting
    reg = r'^[А-ЯЁа-яё ]*:'
    file.readline()
    # creating list with all lines from text
    all_lines = [''.join(x).strip('\n') for x in file.readlines()]
    buffer_list = []
    cnt = 0
    key = ''
    buffer_phrase = ''

    # trying to solve task with for-cycle
    for phrase in all_lines:
        role = ''.join(re.findall(reg, phrase))

        if role != '' and role in roles:
            cnt += 1
            buffer_list.append(make_buffer_list(cnt, role, phrase))
            key = cnt - 1
            buffer_phrase = phrase

        elif role == '':
            buffer_list[key][2] += phrase
            buffer_phrase = ''


for actors in buffer_list:
    db[actors[1]].append(f'{actors[0]}) {actors[2]}')


with open('output.txt', 'w') as file:
    for i in db.items():
        file.write(f'{i[0]}\n')
        for j in i[1]:
            file.write(f'{j}\n')
