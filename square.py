#!/usr/bin/env python3
from math import sqrt
# input 4 tuples representing the ordered pairs of the 4 points, unordered.
def checkForRectangle(point_list):
    a = point_list[0]
    distance_list = []
    for x, y in point_list[1:]:
        distance_list.append(sqrt((x - a[0]) ** 2 + (y - a[1]) ** 2))
        print("{}".format(distance_list[-1]))
    # TODO: check if any distance in distance_list squared is equal to the sum of other distances squared 



# Driver Code
point_list = [(0, 0), (3, 0), (3, 3), (0, 3)]
if checkForRectangle(point_list):
    print("is rectangle")