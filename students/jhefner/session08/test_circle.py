#!/Users/jhefner/python_dev/uw_python/bin/python

"""
circle.py
"""

from circle import Circle

def test_int_input():
    assert Circle(4) #test: circle class can take int input

def test_radius():
    c = Circle(4)
    assert c.radius == 4 #test: validate input radius is accessible by class.

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8 #test: validate diameter calculated to radius.

def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4