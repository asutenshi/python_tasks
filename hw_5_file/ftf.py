roles = []

with open('roles.txt', 'r', encoding='utf-8') as input:
    with open('output.txt', 'r+', encoding='utf-8') as output:
        output.truncate(0)
        input.readline() # line: roles
        i_line = input.readline().strip()
        while i_line != "textLines:":
            role = i_line
            roles.append(role)
            output.write(i_line + ":\n\n")
            i_line = input.readline().strip()
        i_line = input.readline() # for skip line: textLines:
        # while i_line:
        for i in range(2):
            if i_line[0] != ' ':
                print('-2', i_line.strip())
                print('-1', i_line.strip().split(':', 1))
                if i_line.strip().split(':', 1)[-1] == '':
                    i_line = input.readline()
                    continue
                else:
                    temp = i_line.strip().split(':', 1)
                    role = temp[0].strip()
                    print('role: ' + role)
                    rep = temp[1].strip()
                    print('rep: ' + rep)
                    output.seek(0)
                    print(output.tell())
                    o_line = output.readline() # первая строка
                    while o_line.strip()[:-1] != role:
                        o_line = output.readline()
                    while o_line.strip() != '':
                        o_line = output.readline()
                    print('0' + i_line)
                    print('1' + o_line)
                    # o_line = output.readline() # skip role and go to \n str
                    print('2' + o_line)
                    print('3', output.tell())
                    position = output.tell()
                    output.seek(position)
                    output.write(rep)
                    print('4', output.tell())
                    i_line = input.readline()
            else:
                i_line = input.readline()
                continue

# roles = []
#
# with open('roles.txt', 'r', encoding='utf-8') as input:
#     with open('output.txt', 'w', encoding='utf-8') as output_w:
#         output_w.truncate(0)
#         input.readline() # line: roles
#         i_line = input.readline().strip()
#         while i_line != "textLines:":
#             role = i_line
#             roles.append(role)
#             output_w.write(i_line + ":\n\n")
#             i_line = input.readline().strip()
#         i_line = input.readline() # for skip line: textLines:
#         output_w.close()
#         while i_line:
#             if i_line[0] != ' ':
#                 print('-2', i_line.strip())
#                 print('-1', i_line.strip().split(':', 1))
#                 if i_line.strip().split(':', 1)[-1] == '':
#                     i_line = input.readline()
#                     continue
#                 else:
#                     temp = i_line.strip().split(':', 1)
#                     role = temp[0]
#                     rep = temp[1]
#                 with open('output.txt', 'r', encoding='utf-8') as output_r:
#                     o_r_line = output_r.readline() # ?????? ??????
#                     while o_r_line.strip()[:-1] != role:
#                         # while o_r_line.strip() != '':
#                         #     o_line = output_r.readline()
#                         o_r_line = output_r.readline()
#                     print('0' + i_line)
#                     print('1' + o_r_line)
#                     # o_r_line = output_r.readline() # skip role and go to \n str
#                     print('2' + o_r_line)
#                     print('3', output_r.tell())
#                     position = output_r.tell()
#                     output_r.close()
#                     with open('output.txt', 'w', encoding='utf-8') as output_w:
#                         output_w.seek(position)
#                         output_w.write(rep)
#                         print('4', output_w.tell())
#                         output_w.close()
#                     i_line = input.readline()
#             else:
#                 i_line = input.readline()
#                 continue
