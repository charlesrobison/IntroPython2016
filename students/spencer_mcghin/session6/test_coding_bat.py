#!/usr/bin/env python

from coding_bat import sorta_sum


def test_01():
    assert sorta_sum(10, 9)


def test_02():
    assert sorta_sum(3, 3)


def test_03():
    assert sorta_sum(100, -81)


def test_04():
    assert sorta_sum(1, 1)
