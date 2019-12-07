import sys

def runOpcodeOperation(index):
    if opcodeList[index] == 1:
        opcodeList[opcodeList[index + 3]] = opcodeList[opcodeList[index + 1]] + opcodeList[opcodeList[index + 2]]
        runOpcodeOperation(index + 4)
    elif opcodeList[index] == 2:
        opcodeList[opcodeList[index + 3]] = opcodeList[opcodeList[index + 1]] * opcodeList[opcodeList[index + 2]]
        runOpcodeOperation(index + 4)
    elif opcodeList[index] == 99:
        return

verbList = list(range(0,99))
nounList = list(range(0,99))

for i in nounList:
    for j in verbList:
        with open(sys.argv[1]) as f:
            opcodeList = f.readline().split(',')
        opcodeList = [int(i) for i in opcodeList]
        opcodeList[1] = i
        opcodeList[2] = j
        runOpcodeOperation(0)
        if opcodeList[0] == 19690720:
            print("the noun is " + str(i) + " and the verb is " + str(j))
print(opcodeList[0])

