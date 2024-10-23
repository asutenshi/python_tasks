n = int(input())
data = {}

for _ in range(n):
    words = input().lower().split()
    for word in words:
        if word in data: data[word] += 1 
        else: data[word] = 1

# lambda, чтобы сравнение по ключу выводилось в порядке возрастания (наверное так удобнее)
sorting_words = sorted([(value, key) for key, value in data.items()], key=lambda x: (-x[0], x[1]))

# можное еще выводить сколько раз слово встретилось в тексте
for _, word in sorting_words:
    print(word)