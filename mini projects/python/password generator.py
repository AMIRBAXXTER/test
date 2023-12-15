from random import randint
x = int(input("your password length:"))
p = ""
for i in range(x):
    r = chr(randint(33, 126))
    p += r
print("your password is:", p)
