import sys

with open(sys.argv[1]) as f:
    opcodeList = f.readline().split(',')
opcodeList = [int(i) for i in opcodeList]
opcodeList[1] = 12
opcodeList[2] = 2

def runOpcodeOperation(index):
    if opcodeList[index] == 1:
        opcodeList[opcodeList[index + 3]] = opcodeList[opcodeList[index + 1]] + opcodeList[opcodeList[index + 2]]
        runOpcodeOperation(index + 4)
    elif opcodeList[index] == 2:
        opcodeList[opcodeList[index + 3]] = opcodeList[opcodeList[index + 1]] * opcodeList[opcodeList[index + 2]]
        runOpcodeOperation(index + 4)
    elif opcodeList[index] == 99:
        return

runOpcodeOperation(0)
print(opcodeList[0])

