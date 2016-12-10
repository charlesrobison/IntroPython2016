"""
tests for circle.py
run with:
$python3 -m pytest test_circle.py
"""

import math

from circle import Circle


def test_create_circle():
    c = Circle(4)
    assert c.radius == 4


def test_from_diamter():
    c = Circle.from_diameter(8)
    assert c.radius == 4
    assert c.diameter == 8


def test_diameter():
    c = Circle(5)
    assert c.diameter == 10


def test_change_radius():
    c = Circle(5)
    c.radius = 2
    assert c.diameter == 4


def test_set_diameter():
    c = Circle(4)
    c.diameter = 10
    assert c.radius == 5
    assert c.diameter == 10


def test_area():
    c = Circle(3)
    assert c.area == math.pi * 3 ** 2
    # might try writing an assert for raises AttributeError
    # c.area = 5


def test_print():
    c = Circle(4)
    assert c.__str__() == "Circle with radius: 4"


def test_repr():
    c = Circle(4)
    assert c.__repr__() == "Circle(4)"


def test_add():
    c1 = Circle(4)
    c2 = Circle(6)
    new_c = c1 + c2
    assert new_c.radius == 10


def test_mult():
    c = Circle(4)
    c2 = Circle(12)
    assert (c * 3).radius == 12


def test_equal():
    c1 = Circle(4)
    c2 = Circle(4)
    assert c1 == c2


def test_not_equal():
    c1 = Circle(4)
    c2 = Circle(4)
    # this passes no matter what, why?
    assert not c1 != c2


def test_lt():
    c1 = Circle(4)
    c2 = Circle(8)
    assert c1 < c2


def test_gt():
    c1 = Circle(8)
    c2 = Circle(4)
    assert c1 > c2
