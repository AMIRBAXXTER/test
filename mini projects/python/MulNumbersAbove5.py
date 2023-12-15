def mul5(number):
    if number == 0:
        return 1
    elif number % 10 < 5:
        return mul5(number // 10)
    else:
        return number % 10 * mul5(number // 10)


print(mul5(261937))
