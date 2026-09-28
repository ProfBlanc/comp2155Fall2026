from abc import ABC, abstractmethod
# abstract base class

# this class groups common actions of a 2D Shape
class Shape2D(ABC):
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
    def is_long_shape(self):
        return self.width > self.length
    # area, perimeter
    # is there a default formula for ALL shapes
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self): pass

class Rectangle(Shape2D):
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

# s = Shape()
# print(s)
r = Rectangle("Rectangle", 10, 5)
print(r.area())