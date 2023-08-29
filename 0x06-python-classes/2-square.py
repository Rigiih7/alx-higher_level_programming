#!/usr/bin/python3
"""Class Square."""


class Square:
    """Class square."""

    def __init__(self, size=0):
        """object Square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
