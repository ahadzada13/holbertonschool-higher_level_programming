#!/usr/bin/python3
"""
This module defines a Square class.

This module adds validation for the size attribute to ensure it is
a non-negative integer.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        __size (int): The size of the side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance with validation.

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
