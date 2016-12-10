#!/usr/bin/env python3
''' Lambda Keyword
    Functions are created when they are created
'''

# def function_builder(n):
#     l = []
#     for i in range(n):
#         def f(x, inc = i):
#             return x + inc
#         l.append(f)
#     return l
# 
# def function_builder(n):
#     l = []
#     for i in range(n):
#         print('Creating f with :', i)
#         # l.append(lambda x: x + i)
#         l.append(lambda x, inc = i: x + inc)
#     print("i at end of loop:", i)
#     return l

def function_builder(n):
    return [lambda x, inc = i: x + inc for i in range(n)]
