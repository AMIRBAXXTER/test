from functools import wraps


def memoize(func):
    memory = {}

    @wraps(func)
    def inner(n):
        if n not in memory:
            memory[n] = func(n)
        return memory[n]
    return inner

@memoize
def fibonachi(n):
    if n == 0 or n == 1:
        return n
    return fibonachi(n - 1) + fibonachi(n - 2)


print(fibonachi(35))
