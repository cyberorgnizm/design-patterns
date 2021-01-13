import re
from abc import ABC, abstractmethod

class Shape(ABC):
    """An abstract base class for shapes"""
    
    @abstractmethod
    def draw(self):
        ...


class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")


class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")


class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")


class ShapeFactory:
    """A factory to generate object of concrete class based on given information"""

    def get_shape(self, shape_type=None):
        if shape_type is None:
            return None
        elif re.match("CIRCLE", shape_type, flags=re.IGNORECASE):
            return Circle()
        elif re.match("SQUARE", shape_type, flags=re.IGNORECASE):
            return Square()
        elif re.match("RECTANGLE", shape_type, flags=re.IGNORECASE):
            return Rectangle()
        else:
            return None


if __name__ == "__main__":
    factory = ShapeFactory()

    # get instance of a Circle
    circle = factory.get_shape("CIRCLE")
    circle.draw()

    # get instance of square
    square = factory.get_shape("SQUARE")
    square.draw()

    # get instance of Rectangle
    rect = factory.get_shape("RECTANGLE")
    rect.draw()