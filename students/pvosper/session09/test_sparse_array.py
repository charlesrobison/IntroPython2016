#!/usr/bin/env python3

'''
Simple testst for SparseArray
'''

from sparse_array import SparseArray

def test_len():
    sa = SparseArray([7,29,0,0,0,0,13,0,0,72])
    assert len(sa) == 10
    
def test_index():
    sa = SparseArray([7,29,0,0,0,0,13,0,0,72])
    assert sa[1] == 29
    assert sa[2] == 0
    assert sa[9] == 72

# This works (I think) but I can't figure out how to test it
# def test_IndexError():
#     sa = SparseArray([7,29,0,0,0,0,13,0,0,72])
#     assert sa[21] != raises(IndexError)

def test_getvalue():
    sa = SparseArray([7,29,0,0,0,0,13,0,0,72])
    test_a = sa[6]
    test_b = sa[1]
    test_c = sa[5]
    assert test_a == 13
    assert test_b == 29
    assert test_c == 0
    
def test_del():
    sa = SparseArray([7,29,0,0,0,0,13,0,0,72])
    del sa[4]
    assert sa[1] == 29
    assert sa[2] == 0
    assert sa[8] == 72


'''
sa[5] = 12
sa[3] = 0 # the zero won't get stored!
val = sa[13] # it should get a zero if not set

del sa[4]

It should raise an IndexError if you try to access an index beyond the end.
IndexError: list index out of range
it should have an append() method
Can you make it support slicing?
How else can you make it like a list?

['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__imul__',
 '__init__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__rmul__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']
 
'''