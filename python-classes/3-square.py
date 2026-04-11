#!/usr/bin/python3
"""
This module defines a Square class.

This module adds a public method to calculate the area of the square
based on its private size attribute.
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

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
