import functools

n, k = map(int, input().split())

@functools.lru_cache()
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + k * fib(n - 2)

print(fib(n))
