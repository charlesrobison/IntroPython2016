"""

Circle Lab

"""

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return 'Radius: %i, Diameter: %i' % (self.radius, self.diameter)

    def __repr__(self):
        return repr(self.radius)

    def __add__(self, other):
        add_circle = self.radius + other.radius
        return add_circle

    def __mul__(self, other):
        mul_circle = self.radius * other.radius
        return mul_circle

    @property  # computes on the fly as opposed to storing init value
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter=None):
        return diameter
