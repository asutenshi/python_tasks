output = {} # {role: [replic, replic, replic]}

with open('roles.txt', 'r', encoding='utf-8') as input:
    # skip roles: line
    input.readline()  
    i_line = input.readline().strip()
    # write roles into output
    while i_line != "textLines:": 
        role = i_line
        output[role] = []
        i_line = input.readline().strip()
    # skip textLines: line
    i_line = input.readline()
    # count for replicks
    count_rep = 1
    # save current_role
    current_role = ''
    # read while i_line is not ''
    while i_line:
        # если строка нанется с пробела, то в ней нет роли
        if i_line[0] != ' ':
            # role:''
            if i_line.strip().split(':', 1)[-1] == '':
                count_rep += 1
                current_role = i_line.strip().split(':', 1)[0]
                i_line = input.readline()
            # role: rep
            else:
                temp = i_line.strip().split(':', 1)
                role = temp[0].strip()
                rep = temp[1].strip()
                output[role].append(f'{count_rep}) {rep}')
                count_rep += 1
                current_role = role
                i_line = input.readline()
        # строка начинается с пробела
        else:
            rep = i_line.strip()
            # если реплика не закончилась
            if output[current_role] and output[current_role][-1][:len(str(count_rep))] == str(count_rep):
                print(output[current_role][-1])
                output[current_role][-1] += f'    {rep}'
            # если строка началась с пробела, но до нее была строка вида role:''
            else:
                output[current_role].append(f'{count_rep}) {rep}')
            i_line = input.readline()

# запись в output file
with open('output.txt', 'w', encoding='utf-8') as output_f:
    # очищаю output file
    output_f.truncate(0)
    for key, value in output.items():
        output_f.write(f'{key}:\n')
        for rep in value:
            output_f.write(f'{rep}\n')
