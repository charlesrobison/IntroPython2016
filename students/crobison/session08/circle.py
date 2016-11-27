#!/usr/bin/env python3

# Charles Robison
# 2016.11.26
# Circle Lab

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        self = cls()
        return self