#!/usr/bin/env python3

"""Nov 26, 2016 Test cases for args and kwargs lab exercise."""

import pytest
from sm_args_kwargs_lab import color_args_kwargs_t


def test_color_all():
    result = color_args_kwargs_t('yellow', fore_color='green', back_color='orange', link_color='white', visited_color='red')
    print(result)
    assert 'yellow' in result
    assert 'green' in result
    assert 'orange' in result


def test_color_onlykwargs():
    result = color_args_kwargs_t(fore_color='green', back_color='orange', link_color='white', visited_color='red')
    print(result)
    assert 'green' in result
    assert 'orange' in result


def test_color_empty():
    result = color_args_kwargs_t()
    print(result)
    assert ' ' in result
    assert ' ' in result


def test_color_onearg_twokwargs():
    result = color_args_kwargs_t('yellow', link_color='white', visited_color='red')
    print(result)
    assert 'yellow' in result
    assert 'white' in result


def test_color_twokwargs():
    result = color_args_kwargs_t(link_color='white', visited_color='red')
    print(result)
    assert 'white' in result
    assert 'red' in result


def test_color_onearg_twokwargs_othercolor():
    result = color_args_kwargs_t('yellow', other_color='silver', visited_color='red')
    print(result)
    assert 'yellow' in result
    assert 'Key not accepted' in result


def test_color_onearg_fivekwargs_othercolor():
    result = color_args_kwargs_t('yellow', fore_color='green', back_color='orange', link_color='white', visited_color='red', other_color='silver')
    print(result)
    assert 'yellow' in result
    assert 'Key not accepted' in result

# Cannot test SyntaxError.

# def test_color_onearg_twokwargs_repeat():
#     with pytest.raises(SyntaxError):
#         result = color_args_kwargs_t('yellow', fore_color='green', fore_color = 'green')
#         print(result)
#         assert 'green' in result
#         assert 'orange' in result
