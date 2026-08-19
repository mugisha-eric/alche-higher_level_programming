#!/usr/bin/python3
"""Module that defines a Square class that supports comparisons."""


class Square:
    """A class that defines a square that supports comparison operators."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (float or int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with type and value validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square is less than another based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is less than or equal based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square is greater than another based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is greater than or equal based on area."""
        return self.area() >= other.area()
