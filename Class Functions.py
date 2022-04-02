class Square:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height


    def perimeter(self):
        return self.base * 2 + self.height * 2

    def __str__(self):
        return "Square - lenght: {0}".format(self.length)

square1 = Square(4)
print(square1)
print(square1.area())
print(square1.perimeter())


square2 = Square(16)
print(square2)
print(square2.area())
print(square2.perimeter())

class Triangle:
    def __init__(self, base, height, a, b, c):
        self.base = base
        self.height = height
        self.a = a
        self.b = b 
        self.c = c 

    def area(self):
        return (self.base * self.height) / 2
    
    def perimeter(self):
        return self.a + self.b + self.c

triangle = Triangle(5, 10, 10, 20, 30)
print(triangle.area())
print(triangle.perimeter())