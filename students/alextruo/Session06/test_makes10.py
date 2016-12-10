#!/usr/bin/env python

'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
'''

from makes10 import makes10

def test_1():
    assert makes10(9,10) is True

def test_2():
    assert makes10(9,9) is False

def test_3():
    assert makes10(10,1) is True

def test_4():
    assert makes10(10,10) is True

def test_5():
    assert makes10(2,13) is False

def test_6():
    assert makes10(5,5) is True

def test_7():
    assert makes10(6,4) is True

def test_8():
    assert makes10(7,3) is True

def test_9():
    assert makes10(-3, 13) is True

def test_10():
    assert makes10(8,2) is True

def test_11():
    assert makes10(23,21) is False

def test_12():
    assert makes10(25,-2) is False

'''
This is not a correct test, so it will flag as a failure each time.

def test_13():
    assert makes10(9, 1) is False
    '''
'''
This will always fail.

def test_14():
    assert False
'''