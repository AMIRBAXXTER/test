def maximum():
    x = int(input("x :"))
    y = int(input("y :"))
    z = int(input("z :"))
    ma = x
    if x < y:
        ma = y
    if x < z and y < z:
        ma = z
    return ma


print(maximum())
