#!/usr/bin/env python

'''
We have a loud talking parrot. 
The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
Return True if we are in trouble.
'''
from talking_parrot import talking_parrot
#from talking_parrot, import the file as talking_parrot.py


def test_1():
    assert talking_parrot(True, 23) is True

def test_2():
    assert talking_parrot(False, 10) is False

def test_3():
    assert talking_parrot(True, 6) is True

def test_4():
    assert talking_parrot(False, 1) is False

def test_5():
    assert talking_parrot(True, 5) is True

def test_6():
    assert talking_parrot(True, 20) is False

def test_7():
    assert talking_parrot(True, 21) is True

def test_8():
    assert talking_parrot(True, 1) is True

def test_9():
    assert talking_parrot(True, 3) is True

def test_10():
    assert talking_parrot(False, 12) is False

def test_11():
    assert talking_parrot(False, 1) is False

#This fails because the test does not meet the defined function; this should be True, we are in trouble
#def test)12():
 #   assert talking_parrot(True, 2) is False
#This will always fail because I chose False as the assert.
#def test_12():
 #   assert False 