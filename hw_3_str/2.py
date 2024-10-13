n, m = map(int, input("Введите m и n: ").split())
s = input("Введите строку: ")
words = set()

for i in range(n):
    temp = [s[i:][j:j+m] for j in range(0, n, m)]
    for word in temp:
       if len(word) == m:
           words.add(word) 
    n -= 1
print(len(words), words)
