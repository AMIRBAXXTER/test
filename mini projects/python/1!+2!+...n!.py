def f(x):
    y = 1
    for i in range(1, x+1):
        y *= i
    return y


def sum_f(x):
    w = 0
    for i in range(1, x+1):
        w += f(i)
    return w


x = int(input("number:"))
print(sum_f(x))
