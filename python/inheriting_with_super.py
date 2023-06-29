""" Shows how to inherit using super """

class A:
    def __init__(self):
        self.x = 1
        self.y = 2

class B(A):
    def __init__(self):
        super().__init__()
        self.z = 3

    def __str__(self):
        return f"x: {self.x}\ny: {self.y}\nz: {self.z}"

print(B())
