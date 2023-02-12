#!/usr/bin/python3
"""Testing for pie of a cirlce"""

from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError("the number cannot be less than zero")
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a real positive number")
    return pi*(r**2)

#Test Function
# radii = [2, 0, -1, 2 + 5j, True, "radius"]
# msg = "Area of circles with r = {radius} is {area}"

# for r in radii:
#     A = circle_area(r)
#     print(msg.format(radius = r, area = A))