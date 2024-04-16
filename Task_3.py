"""Создайте функцию генератор чисел Фибоначчи"""


def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print(list(fib(13)))
