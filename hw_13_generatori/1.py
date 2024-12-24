def fibonachiNumbers(n):
    yield 0
    yield 1
    fib_numbers = [0, 1]
    for i in range(n):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        yield fib_numbers[-1]

n = int(input('Введите кол-во чисел Фибоначчи: '))
fn = fibonachiNumbers(n)

for i in range(n):
    print(next(fn), end=' ')
