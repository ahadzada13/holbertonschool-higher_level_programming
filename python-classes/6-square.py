#!/usr/bin/python3
"""
This module defines a Square class.

This module implements a Square class with private size and position
attributes, including getters, setters, and a method to print the square
at a specific coordinate.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        __size (int): The size of the side of the square.
        __position (tuple): The (x, y) coordinates of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square instance.

        Args:
            size (int): The length of the side of the square.
            position (tuple): The (x, y) coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the private position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the private position attribute with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the '#' character to stdout.

        The square is offset by the position attribute.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print the empty lines for the y-coordinate
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print()

        # Print each row of the square
        for _ in range(self.__size):
            # Print the spaces for the x-coordinate
            print(" " * self.__position[0] + "#" * self.__size)
