class point:
    def __init__(self, x: float = 0, y: float = 0):
        self.move(x, y)

    def move(self, x: float, y: float) -> None:

        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def set_x_y(self, x, y):
        if x == int(x):
            self.x = x
        else:
            print("x value not set")
        if y == int(y):
            self.y = y
        else:
            print("y value not set")

    def get_x_y(self):
        return f"x is : {self.x}\ny is : {self.y}"


def main():
    p1 = point()
    p1.set_x_y(4, 7)
    print(p1.get_x_y())


if __name__ == "__main__":
    main()
