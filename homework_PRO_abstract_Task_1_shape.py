from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def perimeter(self):
        return 2 * pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = self.perimeter()/2
        return (p * ((p - self.a) * (p - self.b) * (p - self.c))) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


def main():
    r = float(input('Radius: '))
    circle = Circle(r)
    print(f'circle area: {circle.area(): .2f}')
    print(f'circle perimeter: {circle.perimeter(): .2f}')

    a, b, c = float(input('Side a: ')), float(input('Side b: ')), float(input('Side c: '))
    triangle = Triangle(a, b, c)
    print(f'triangle area: {triangle.area(): .2f}')
    print(f'triangle perimeter: {triangle.perimeter(): .2f}')

    a, b = float(input('width: ')), float(input('height: '))
    rectangle = Rectangle(a, b)
    print(f'rectangle area: {rectangle.area(): .2f}')
    print(f'rectangle perimeter: {rectangle.perimeter(): .2f}')


if __name__ == '__main__':
    main()

























