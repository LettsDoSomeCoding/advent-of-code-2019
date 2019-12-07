import sys

wireLocation1 = [0,0]
wireLocation2 = [0,0]
directions1 = []
directions2 = []

def move_one_step(step, startingLocation):
    if step[0] == 'R':
        startingLocation[0] = startingLocation[0] + int(step[1:])
    elif step[0] == 'L':
        startingLocation[0] = startingLocation[0] - int(step[1:])
    elif step[0] == 'U':
        startingLocation[1] = startingLocation[1] + int(step[1:])
    elif step[0] == 'D':
        startingLocation[1] = startingLocation[1] - int(step[1:])


with open(sys.argv[1]) as f:
    for i,line in enumerate(f):
        if i == 0:
            directions1 = line.split(',')
        elif i == 1:
            directions2 = line.split(',')

for step1,step2 in zip(directions1,directions2):
    move_one_step(step1,wireLocation1)
    move_one_step(step2,wireLocation2)

    if wireLocation1 == wireLocation2:
        distance = abs(wireLocation1[0]) + abs(wireLocation1[1])
        print("There is an intersection point at [" + str(wireLocation1[0]) + "," + str(wireLocation1[1]) + " which has a Manhattan distance of " + str(distance))

print("finish")