class Color:
    def __init__(self, name: str, rgb: int):
        self.name = name
        self.rgb = rgb

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if name:
            self._name = name
        else:
            print("invalid name!...")

    @name.deleter
    def name(self):
        del self._name
        print("name delete")


c = Color("555", 12345)
print(c.name)
print(c.rgb)

