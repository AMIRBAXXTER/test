class Base:
    num_base_calls = 0

    def call_me(self):
        print("call base class")
        Base.num_base_calls += 1


class RightSubClass(Base):
    num_right_calls = 0

    def call_me(self):
        Base.call_me(self)
        print("call right class")
        RightSubClass.num_right_calls += 1


class LeftSubClass(Base):
    num_left_calls = 0

    def call_me(self):
        Base.call_me(self)
        print("call left class")
        LeftSubClass.num_left_calls += 1


class SubClass(RightSubClass, LeftSubClass):
    num_sub_calls = 0

    def call_me(self):
        RightSubClass.call_me(self)
        LeftSubClass.call_me(self)
        print("call sub class")
        SubClass.num_sub_calls += 1


obj = SubClass()
obj.call_me()
print(obj.num_base_calls)
print(obj.num_right_calls)
print(obj.num_left_calls)
print(obj.num_sub_calls)

