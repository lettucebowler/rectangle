#!/usr/bin/env python3
from math import sqrt

# input 4 tuples representing the ordered pairs of the 4 points, unordered.
def checkForRectangle(point_list):
    is_rectangle = False
    if len(point_list)  != 4:
        return false

    a = point_list[0]
    distance_list = []
    for x, y in point_list[1:]:
        distance_list.append(sqrt((x - a[0]) ** 2 + (y - a[1]) ** 2))
        print("{}".format(distance_list[-1]))

    distance_list = sorted(distance_list, reverse=True)
    return distance_list[0] == sqrt((distance_list[1] ** 2 + distance_list[2] ** 2))

# Driver Code
point_list = [(0, 0), (4, 3), (-6, 8), (-2, 11)]

if checkForRectangle(point_list):
    print("is rectangle" + str(2 ** 2))