class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value:
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"len : {len(value)}")

    def __delete__(self, instance):
        del self.name


class Parent:
    child_name = NameDescriptor()
    father_name = NameDescriptor()
    mother_name = NameDescriptor()

    def __init__(self, child, father, mother):
        self.child_name = child
        self.father_name = father
        self.mother_name = mother


p = Parent("ahmad", "reza", "maryam")
print(p.child_name)
print(p.father_name)
print(p.mother_name)
print(p.__dict__)
