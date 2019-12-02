import sys

opcodeList = sys.argv[1].split(',')
opcodeList = list(map(int, opcodeList))
opcodeList[1] = 12
opcodeList[2] = 2


def runOpcodeOperation(index):
    if opcodeList[index] == 1:
        opcodeList[opcodeList[index + 3]] = opcodeList[index + 1] + opcodeList[index + 2]
        runOpcodeOperation(index + 4)
    elif opcodeList[index] == 2:
        opcodeList[opcodeList[index + 3]] = opcodeList[index + 1] * opcodeList[index + 2]
        runOpcodeOperation(index + 4)
    elif opcodeList[index] == 99:
        return

runOpcodeOperation(0)
print(opcodeList[0])

