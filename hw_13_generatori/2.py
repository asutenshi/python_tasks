n = int(input('Введите число, для которого нужно найти все простые множители: '))

multipliers = [x for x in range(1, int(n / 2) + 1) if n % x == 0 and x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

for _, mult in enumerate(multipliers):
    print(mult)

