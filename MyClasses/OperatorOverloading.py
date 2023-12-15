class NewInteger(int):
    def __init__(self, number):
        self.number = number

    def __add__(self, *other):
        s = self.number
        for i in other:
            s = self.number + i.number
        return NewInteger(s)


num1 = NewInteger(5)
num2 = NewInteger(10)
num3 = NewInteger(15)
num4 = NewInteger(20)
num5 = NewInteger(25)

sum_num = num1 + num2 + num3 + num4 + num5
print(type(sum_num))
print(sum_num)
