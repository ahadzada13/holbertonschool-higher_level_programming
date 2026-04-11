#!/usr/bin/python3
"""
This module defines a Square class.

This module provides a basic Square class that stores a private size attribute.
The purpose is to demonstrate encapsulation in Python, where attributes are
kept private to control how they are accessed and modified.
"""


class Square:
    """
    A class used to represent a Square.

    Attributes:
        __size (int): The size of the side of the square. It is a private
        instance attribute to ensure data integrity.
    """

    def __init__(self, size):
        """
        Initializes the Square instance with a specific size.

        Args:
            size (int): The length of the side of the square.
            This value is stored privately for future validation logic.
        """
        self.__size = size
