import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def __add__(self, other):
        new_radius = self.radius + other.radius
        return Circle(new_radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __mul__(self, num):
        return Circle(self.radius * num)

    def __ne__(self, other):
        return self.radius != other.radius

    __rmul__ = __mul__

    def __repr__(self):
        return "Circle(" + str(self.radius) + ")"

    def __str__(self):
        return "Circle with radius: " + str(self.radius)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2.0

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter / 2.0)
        return self
