factorial = lambda n: 1 if n == 1 else n * factorial(n - 1)


def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


tail_factorial = lambda n, s=1: s if n == 1 else tail_factorial(n - 1, s * n)


def tail_factorial(n: int, s: int = 1) -> int:
    if n == 1:
        return s
    else:
        tail_factorial(n - 1, s * n)


def loop_factorial(n: int) -> int:
    i, res = 1, 1
    while i != n:
        i += 1
        res *= i
    return res
