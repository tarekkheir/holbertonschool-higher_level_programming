#!/usr/bin/python3
"""
Inheritance module - task 4
"""


class BaseGeometry():
    """Class BaseGeometry"""
    def area(self):
        """raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raise conditions"""
        if not isinstance(name, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
