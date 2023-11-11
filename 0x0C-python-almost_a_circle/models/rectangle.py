#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.validate_non_negative_int(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.validate_non_negative_int(value, "height")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.validate_non_negative_int(value, "x")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.validate_non_negative_int(value, "y")
        self.__y = value

    def validate_non_negative_int(self, value, attribute):
        """Validate if value is a non-negative integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle with '#' characters"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """String representation of the object"""
        return "[Rectangle] ({}) {}/{}} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """Updates attributes with no-keyword arguments"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the object"""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }
