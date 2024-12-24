a = int(input('Введите число а: '))
b = int(input('Введите число b: '))

def primeAB(a, b):
    for x in range(a, b+1):
        if all([x % i != 0 for i in range(2, int(x**0.5) + 1)]):
            yield x

pab = primeAB(a, b)
list_ = list(pab)
print(f'Простые числа от {a} до {b}: {list_}')
