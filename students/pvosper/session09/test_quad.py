#!/usr/bin/env python3

'''
Quad

Write a class for a quadratic equation.

The initializer for that class should take the parameters: a, b, c
It should store those parameters as attributes.
The resulting instance should evaluate the function when called, and return the result:
my_quad = Quadratic(a=2, b=3, c=1)

my_quad(0)

'''

from quad import Quadratic

def test_dis_pos():
    my_quad = Quadratic(2, 3, 1)
    assert my_quad.dis == 1
    assert my_quad.x1 == -2.0
    assert my_quad.x2 == -4.0

def test_dis_neg():
    my_quad = Quadratic(1, 2, 3)
    assert my_quad.dis == -8

def test_dis_zero():
    my_quad = Quadratic(1, 2, 1)
    assert my_quad.dis == 0
    assert my_quad.x == -1.0