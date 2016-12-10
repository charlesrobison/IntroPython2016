"""
tests for sparse_array.py
run with:
$python3 -m pytest test_sparse_array.py
"""

from sparse_array import SparseArray

def test_basic_sparse_array():
    sa = SparseArray([1, 0, 4, 0, 0, 5, 0, 6])


def test_len():
    sa = SparseArray([1, 0, 4, 0, 0, 5, 0, 6])
    assert len(sa) == 8


def test_index():
    sa1 = SparseArray([1, 0, 4, 0, 0, 5, 0, 6])
    sa2 = SparseArray([0, 3, 6, 3, 0, 0, 8, 0, 9, 0, 0])
    assert sa1[1] == 0
    assert sa2[10] == 0
    assert sa1[5] == 5
    print(sa2[3], sa2[4], sa2[5])
    assert sa2[3] == 3


def test_set_item():
    sa = SparseArray([1, 0, 4, 0, 0, 5, 0, 6])
    assert sa[1] == 0
    sa[1] = 2
    assert sa[1] == 2
    print("pre addition: " + str(len(sa)))
    sa[10] = 0
    print(len(sa))
    print(sa[10])
    assert sa[8] == 0
    assert sa[10] == 0


def test_delete():
    sa = SparseArray([1, 2, 3, 4])
    del sa[2]
    assert sa[1] == 2
    assert sa[2] == 4
    sa2 = SparseArray([1, 0, 0, 4, 5, 3])
    del sa2[1]
    print(sa2)
    assert sa2[2] == 4


def test_append():
    sa = SparseArray([1, 2])
    sa.append(3)
    assert len(sa) == 3
    assert sa[2] == 3


def test_in():
    sa = SparseArray([1, 2, 0, 3])
    assert 1 in sa
    assert 0 in sa
    assert 6 not in sa
