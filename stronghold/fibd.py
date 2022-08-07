import functools

n, m = map(int, input().split())

@functools.lru_cache()
def fib(n):
    if n < 0:
        return 0
    elif n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2) - fib(n - (m + 1))

print(fib(n))