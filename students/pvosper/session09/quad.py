#!/usr/bin/env python3

'''
Quad

Write a class for a quadratic equation.

The initializer for that class should take the parameters: a, b, c
It should store those parameters as attributes.
The resulting instance should evaluate the function when called, and return the result:
my_quad = Quadratic(a=2, b=3, c=1)

my_quad(0)

---

ax^2 + bx + c = 0

x = (-b +/- sqrt(b^2 - 4ac))/2a

discriminant = b^2 - 4ac

if Δ > 0, the polynomial has two real roots, if Δ = 0, the polynomial has one
real double root, and if Δ < 0, the two roots of the polynomial are complex
conjugates.

quadratic coefficient, the linear coefficient and the constant or free term.

'''

import math

class Quadratic:
    def __init__(self, a, b, c):
        self.q_coe = a  # quadratic coefficient
        self.q_lin = b  # linear coefficient
        self.con = c    # constant
        self.dis = self.q_lin ** 2 - 4 * self.q_coe * self.con  # discriminant
        print(self.dis)
        
        if self.dis < 0:
            print('The two roots of the polynomial are complex conjugates')
        elif self.dis == 0:
            self.x = (-b + math.sqrt(self.dis)) / (2 * a)
            print('The polynomial has one real double root: ', self.x)
        else:
            self.x1 = (-b + math.sqrt(self.dis)) / 2 * a
            self.x2 = (-b - math.sqrt(self.dis)) / 2 * a
            print('The polynomial has two real roots:', self.x1, 'and', self.x2)