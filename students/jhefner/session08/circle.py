#!/Users/jhefner/python_dev/uw_python/bin/python

"""
circle lab
"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius*2

    @diameter.setter
    def diameter(self, val):
        self.radius=val/2

    @property
    def area(self):
        """this property is ready only because we defined
        a property above but didnt create a getter or setter"""
        return self.radius**2 * math.pi

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter/2)
        return self
