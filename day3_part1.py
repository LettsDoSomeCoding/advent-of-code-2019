import sys
# from sympy import *
from sympy.geometry import Point,Line

wireLocation1 = Point(0,0)
wireLocation2 = Point(0,0)
directions1 = []
directions2 = []

def move_one_step(step, startingLocation):
    finishingLocation = Point(0,0)
    
    if step[0] == 'R':
        finishingLocation = startingLocation.translate(int(step[1:]))
    elif step[0] == 'L':
        finishingLocation = startingLocation.translate(-int(step[1:]))
    elif step[0] == 'U':
        finishingLocation = startingLocation.translate(0, int(step[1:]))
    elif step[0] == 'D':
        finishingLocation = startingLocation.translate(0, -int(step[1:]))
    
    return finishingLocation

with open(sys.argv[1]) as f:
    for i,line in enumerate(f):
        if i == 0:
            directions1 = line.split(',')
        elif i == 1:
            directions2 = line.split(',')

locations1 = []
locations2 = []

for step1,step2 in zip(directions1,directions2):
    wireLocation1 = move_one_step(step1,wireLocation1)
    locations1.append(wireLocation1)
    wireLocation2 = move_one_step(step2,wireLocation2)
    locations2.append(wireLocation2)

lines1 = []
lines2 = []

for location in locations1:
    if locations1.index(location) != len(locations1) - 1:
        line = Line(location,locations1[locations1.index(location) + 1])
        lines1.append(line)

for location in locations2:
    if locations2.index(location) != len(locations2) - 1:
        line = Line(location,locations2[locations2.index(location) + 1])
        lines2.append(line)

for line1 in lines1:
    for line2 in lines2:
        intersectionPoint = line1.intersection(line2)
        print(str(intersectionPoint))

print("finish")