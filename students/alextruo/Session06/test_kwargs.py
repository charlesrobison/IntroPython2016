#!/usr/bin/env python3

"""
Test code for the kwargs lab from Session06
"""

#import the file, and then import these two functions, colors, and call_colors
from kwargs import colors, call_colors

#using just positional  with red, blue, yellow, and chartreuse
def test_positional():
    end_result = colors("red", "blue", "yellow", "chartreuse")
    #this prints the end result object with the input arguments here
    print(end_result)
    assert "red" in end_result
    assert "blue" in end_result
    assert "yellow" in end_result
    assert "chartreuse" in end_result

#use keyword arguments for link_color="red" and back)_color="blue"
def test_keyword_arguments():
    end_result = colors(link_color = "red", back_color = "blue")
    print(end_result)
    assert  "link is red" in end_result
    assert "background is blue" in end_result

#use positional and keyword with purple as positional, and link_color="red" and back_color="blue" as keyword arguments
def test_positional_keyword_combo():
    end_result = colors("purple", link_color="red", back_color="blue")
    print(end_result)
    assert "purple" in end_result
    assert "ink is red" in end_result
    assert "background is blue" in end_result

#use  a dictionary as the argument to test if these are in ithe output
def test_dictonary():
    kwargs = {"fore_color": "orange", "visited_color": "aquamarine", "link_color": "jade", "back_color": "magenta",}
    end_result = colors(**kwargs)
    print(end_result)
    assert "foreground is orange" in end_result
    assert "visited link is aquamarine" in end_result
    assert "background is magenta" in end_result
    assert "link is jade" in end_result

#using a tuple to see if they are in the output
def test_tuple():
    args = ("orange", "yellow", "green", "black")
    end_result = colors(*args)
    print(end_result)
    assert "orange" in end_result
    assert "yellow" in end_result
    assert "green" in end_result
    assert "black" in end_result

#use a tuple and a dictionary
def test_tuple_dictionary():
    args = ("orange", "yellow")
    kwargs = {"link_color": "jade", "visited_color":"violet"}
    #use the positional arguments and the key arguments in kwargs
    end_result = colors(*args, **kwargs)
    print(end_result)
    assert "orange" in end_result
    assert "yellow" in end_result
    assert "link is jade" in end_result
    assert "visited link is violet" in end_result

#test positional for the all_colors function using args* and kwargs**
def test_positional_call_colors():
    args, kwargs = call_colors("white", "teal", "sepia", "baby blue")
    #checks only the args, not kwargs
    assert not kwargs
    assert args == ("white", "teal", "sepia", "baby blue")

def test_keyword_call_colors():
    args, kwargs = call_colors(link_color="rose", visited_color="black", fore_color="stripes")
    #checks the kwargs, not the args
    assert not args
    assert kwargs["link_color"] == "rose"
    assert kwargs["visited_color"] == "black"
    assert kwargs["fore_color"] == "stripes"
    assert len(kwargs) == 3


def test_positional_and_keyword_call_colors():
    args, kwargs = call_colors('teal', 'salmon', link_color='cobalt', back_color="ice")
    #checks the args (positional) and the kwargs (key arguments)
    assert args == ("teal", "salmon")
    assert kwargs == {"link_color": "cobalt", "back_color": "ice"}
