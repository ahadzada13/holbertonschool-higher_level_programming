#!/usr/bin/python3
"""
This module defines a Square class.

This module adds a public method to print the square using the '#' character,
providing a visual representation of the square object.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        __size (int): The size of the side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Args:
            size (int): The length of the side of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the private size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the private size attribute with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the '#' character to stdout.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)
