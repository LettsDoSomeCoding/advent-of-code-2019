import sys

# from sympy import *
from sympy.geometry import Point, Segment

origin = Point(0, 0)
wireLocation1 = Point(0, 0)
wireLocation2 = Point(0, 0)
directions1 = []
directions2 = []


def move_one_step(step, startingLocation, distanceCounter):
    wirePoints = {}

    if step[0] == "R":
        for i in range(int(step[1:])):
            wirePoints[startingLocation.translate(i + 1, 0)] = distanceCounter + i + 1
        startingLocation = startingLocation.translate(int(step[1:]), 0)
    elif step[0] == "L":
        for i in range(int(step[1:])):
            wirePoints[startingLocation.translate(-i - 1, 0)] = distanceCounter + i + 1
        startingLocation = startingLocation.translate(-int(step[1:]), 0)
    elif step[0] == "U":
        for i in range(int(step[1:])):
            wirePoints[startingLocation.translate(0, i + 1)] = distanceCounter + i + 1
        startingLocation = startingLocation.translate(0, int(step[1:]))
    elif step[0] == "D":
        for i in range(int(step[1:])):
            wirePoints[startingLocation.translate(0, -i - 1)] = distanceCounter + i + 1
        startingLocation = startingLocation.translate(0, -int(step[1:]))

    return wirePoints


with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        if i == 0:
            directions1 = line.split(",")
        elif i == 1:
            directions2 = line.split(",")

locations1 = {}
locations2 = {}
print("creating wiremaps")
distanceCounter1 = 0
for step in directions1:
    locations1.update(move_one_step(step, wireLocation1, distanceCounter1))
print("wiremap1 complete")

distanceCounter2 = 0
for step in directions2:
    locations2.update(move_one_step(step, wireLocation2, distanceCounter2))
print("wiremap2 complete")

print("Getting the intersecting points")
intersections = set(locations1.keys()).intersection(locations2.keys())

intersectionDistanceList = []
wireLengthList = []
print("calculating the distances from the intersection points")
for i in intersections:
    intersectionDistanceList.append(origin.taxicab_distance(i))
    wireLengthList.append(locations1.get(i) + locations2.get(i))

print("The shortest intersection distance is " + str(min(intersectionDistanceList)))
print("The shortest overall wire length is " + str(min(wireLengthList)))
