"""

Tests for Circle Classes

"""

from Circle import Circle

from math import pi


def test_radius():
    c = Circle(4)
    assert c.radius == 4


def test_diameter():
    c = Circle(5)
    assert c.diameter == 10


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
    assert c.area == pi * 4 ** 2