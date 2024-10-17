def get_substrings(s, n, m):
    substrings = []
    for i in range(n):
        temp = [s[i:][j:j+m] for j in range(0, n, m)]
        substrings.extend(temp)
        n -= 1
    return substrings

n, m = map(int, input("Введите m и n: ").split())
s = input("Введите строку: ")
words = set()

# Вызов вспомогательной функции
substrings = get_substrings(s, n, m)

for word in substrings:
    if len(word) == m:
        words.add(word)

print(len(words))
