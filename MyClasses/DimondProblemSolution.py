class Base:
    num_base_calls = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def call_me(self):
        print("call base class")
        Base.num_base_calls += 1


class LeftSubClass(Base):
    num_left_calls = 0

    def __init__(self, c, **kwargs):
        # super().__init__(*args)
        super().__init__(**kwargs)
        self.c = c

    def call_me(self):
        super().call_me()
        print("call left class")
        LeftSubClass.num_left_calls += 1


class RightSubClass(Base):
    num_right_calls = 0

    def __init__(self, d, e, f, **kwargs):
        # super().__init__(*args)
        super().__init__(**kwargs)
        self.d = d
        self.e = e
        self.f = f

    def call_me(self):
        super().call_me()
        print("call right class")
        RightSubClass.num_right_calls += 1


class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0

    def __init__(self, g, **kwargs):
        # super().__init__(*args)
        super().__init__(**kwargs)
        self.g = g

    def call_me(self):
        super().call_me()
        print("call sub class")
        SubClass.num_sub_calls += 1


obj = SubClass(a=1, b=2, c=3, d=4, e=5, f=6, g=7)
obj.call_me()
print(obj.num_base_calls)
print(obj.num_right_calls)
print(obj.num_left_calls)
print(obj.num_sub_calls)
print(obj.a, obj.b, obj.c, obj.d, obj.e, obj.f, obj.g)
