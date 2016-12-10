"""
Test for circle class
"""
import math
from circle import Circle, Sphere

def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_diameter():
    c = Circle(5)
    assert c.diameter  == 10

def test_change_radius():
    c = Circle(5)
    c.radius = 2
    assert c.diameter == 4

def test_change_diameter():
    c = Circle(5)
    c.diameter = 12
    assert c.diameter == 12
    assert c.radius == 6

def test_area():
    c = Circle(4)
    assert c.area == math.pi * 4 ** 2

def test_from_diameter():
    c = Circle.from_diameter(8)

    assert c.diameter == 8
    assert c.radius == 4

def test_sphere():
    s = Sphere(4)

    print(s.volume())

    assert s.volume() == 268.0825731006329

def test_sphere_diameter():
    s = Sphere.from_diameter(8)

    print(s.volume())

    assert False