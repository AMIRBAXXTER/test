li = input("enter your number list:").split(",")
li = list(map(int, li))
print(li)
n = list(filter(lambda x: x % 2 == 0, li))
print("even:", n)
m = list(filter(lambda x: x % 2 != 0, li))
print("odd:", m)