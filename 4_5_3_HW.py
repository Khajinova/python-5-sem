import numpy as np

class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def area(self):
        return np.pi * self.radius ** 2

    def perimeter(self):
        return 2 * np.pi * self.radius

    def __str__(self):
        return f"окружность с центром в точке {(self.x, self.y)} и радиусом равным {self.radius}"

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def __str__(self):
        return f" прямоугольник ({self.a} x {self.b})"
    
class Square(Shape):
    def __init__(self, a):
        self.a = a
        

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return 2 * (self.a + self.a)

    def __str__(self):
        return f" квадратик ({self.a} x {self.b})"

class Romb(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
    
    def area(self):
        return 1/2 * np.sqrt((self.x1-self.x3) ** 2 + (self.y1-self.y3) ** 2) * np.sqrt((self.x2-self.x4) ** 2 + (self.y2-self.y4) ** 2)

    def perimeter(self):
        return np.sqrt((self.x1-self.x2) ** 2 + (self.y1-self.y2) ** 2) * 4
    
    def __str__(self):
        return f" робмбик (({self.x1} x {self.y1}, ({self.x2} x {self.y2}), ({self.x3} x {self.y3}), ({self.x4} x {self.y4}))"
