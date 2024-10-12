from random import randint
l = [randint(-100, 101) for _ in range(100)]
print(sorted(l, key=lambda x: sum(map(int, str(x).split()))))