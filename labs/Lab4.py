# Name:matthew
# Period: 6th
# Date:10/10

# Write a function determineQuadrant() that takes two int parameters
# representing the x and y coordinates of the point and determines
# the quadrant in which the point lies.
"""
def determineQuadrant(x,y):
    if x > 0:
        if y>0:
            print("Quadrant 1")
        if y<0:
            print("Quadrant 4")
    if x < 0:
        if y>0:
            print("Quadrant 2")
        if y<0:
            print("Quadrant 3")
    else:
        print("0")
"""
def determineQuadrant(x,y):
    if x > 0 and y>0:
        return("Quadrant 1")
    if x> 0 and y<0:
        return("Quadrant 4")
    if x < 0 and y>0:
        return("Quadrant 2")
    if x < 0 and y<0:
        return("Quadrant 3")
    else:
        return("0")
