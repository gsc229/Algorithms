def fibonacci(n, cache):
    if n < 2:
        return n
    elif cache[n] > 0:
        return cache[n]
    else:
        cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
        return cache[n]


print(fibonacci(900, {i: 0 for i in range(901)}))


def fib(n):
    if n < 2:
        return n
    elif n > 0:
        return
