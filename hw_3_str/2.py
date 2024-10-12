n, m = map(int, input("Введите m и n: ").split())
s = input("Введите строку: ")
words = set()

for i in range(n):
    s_temp = s[i:-1]
    for j in range(0, n, 3):
        word = s_temp[i:i+3]
        if len(word) == 3:
            words.add(s_temp[i:i+3])
    n -= 1
print(words)