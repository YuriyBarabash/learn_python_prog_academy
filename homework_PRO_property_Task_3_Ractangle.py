class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        raise AttributeError("Cannot directly modify width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        raise AttributeError("Cannot directly modify height")

    def calculate_area(self):
        return self.__width * self.__height


rectangle = Rectangle(width=20, height=30)

try:
    rectangle.width = 8
except AttributeError as e:
    print(e)

try:
    rectangle.height = 20
except AttributeError as e:
    print(e)

try:
    rectangle.multiply_of_sides
except AttributeError as e:
    print(e)

area = rectangle.calculate_area()

print(f"Area of the rectangle: {area}")
