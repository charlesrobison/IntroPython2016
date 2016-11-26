#!/usr/bin/env python3

# Charles Robison
# 2016.11.26
# Circle Lab

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diamater(self, val):
        self.radius = val / 2