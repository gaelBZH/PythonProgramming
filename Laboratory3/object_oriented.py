from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == int or float:
            return Point(other * self.x, other * self.y)
        else:
            raise TypeError(type(other), "is not supported for multiplication.")

    def __truediv__(self, other):
        if type(other) == int or float:
            return Point(self.x / other, self.y / other)
        else:
            raise TypeError(type(other), "is not supported for multiplication.")

    def __pow__(self, n):
        result = self.getCopy()
        for i in range(1, n):
            result *= self
        return result

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def getCopy(self):
        return Point(self.x, self.y)
    

A = Point(1,2)
B = Point(5,-1)
C = Point(4, 5)
print(f"A = {A}")
print(f"B = {B}")
print(f"{A} + {B} = {A + B}")
print(f"{B} - {A} = {B - A}")
print(f"{A} * {2} = {A*2}")
print(f"{A} / {2} = {A/2}")
print(f"|{A}| = {abs(A)}")
