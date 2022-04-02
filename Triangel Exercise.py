from random import triangular
import re


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
print(triangle)
print(triangle.area())
print(triangle.perimeter())
    

