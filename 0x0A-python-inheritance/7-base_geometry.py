#!/usr/bin/python3
"""a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry():
    """Class with public instance methods"""

    def area(self):
        raise Exception("area() is not implemented")
        """Raises an Exception with the following message
        """

    def integer_validator(self, name, value):
        """Validates value."""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
