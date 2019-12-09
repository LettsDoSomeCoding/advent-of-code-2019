import sys
# from sympy import *
from sympy.geometry import Point,Segment

origin = Point(0,0)
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

segments1 = []
segments2 = []

for location in locations1:
    if locations1.index(location) != len(locations1) - 1:
        segment = Segment(location,locations1[locations1.index(location) + 1])
        segments1.append(segment)

for location in locations2:
    if locations2.index(location) != len(locations2) - 1:
        segment = Segment(location,locations2[locations2.index(location) + 1])
        segments2.append(segment)

instersectionDistanceList = []

for segment1 in segments1:
    for segment2 in segments2:
        intersectionPoint = segment1.intersection(segment2)
        if str(intersectionPoint) != "[]":
            intersectionDistance = origin.taxicab_distance(intersectionPoint[0])
            instersectionDistanceList.append(intersectionDistance)

print("The shortest intersection distance is " + str(min(instersectionDistanceList)))