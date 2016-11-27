#!/usr/bin/env python3

# Charles Robison
# 2016.11.26
# Circle Lab

from circle import Circle
import math

def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_set_diameter():
    c = Circle(4)
    c.diameter = 10
    assert c.diameter == 10
    assert c.radius == 5

def test_area():
    c = Circle(4)
    assert c.area == math.pi * 4 ** 2

def test_diameter_circle():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

