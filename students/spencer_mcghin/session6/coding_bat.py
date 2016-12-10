#!/usr/bin/env python


# Examples from coding bat - sorta_sum
def sorta_sum(a, b):
    if a + b in range(10, 20):
        return 20
    else:
        return a + b


print(sorta_sum(10, 9))