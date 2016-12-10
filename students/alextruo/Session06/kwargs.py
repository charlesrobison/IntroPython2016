#!/usr/bin/env python

'''
kwargs lab
'''

def colors(fore_color='red', back_color='white', link_color='blue', visited_color='pink'):
    color_output = ("The color arguments are the following:\n"
              "The foreground is {fore_color}\n"
              "The background is {back_color}\n"
              "The link is {link_color}\n"
              "The visited link is {visited_color}").format(fore_color=fore_color, back_color=back_color, link_color=link_color, visited_color=visited_color)
    return color_output

#Write a the same function with the parameters as: *args and **kwargs

def call_colors(*args, **kwargs):
    return args, kwargs