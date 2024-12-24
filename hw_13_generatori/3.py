n = int(input('Введите число n, которое хотите возвести в степень: '))
x = int(input('Введите степень, до которой нужно возводить чилос n: '))

def fastpow(n, x):
    for p in range(x + 1):
        yield n ** p

fp = fastpow(n, x)

for i in range(x):
    print(f'{n}^{i}={next(fp)}')
