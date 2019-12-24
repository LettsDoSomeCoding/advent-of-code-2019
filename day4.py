passwordRange = range(231832,767346)

def check_double_digits(numberString):
    for char in set(numberString):
        if (numberString.count(char * 4) > 0 or 
            (numberString.count(char * 3) == 1 and numberString.count(char * 2) == 1) or
            (numberString.count(char * 2) == 0)):
            continue
        return True
    return False

def check_never_decrease(numberString):
    numberList = []
    for char in numberString:
        numberList.append(int(char))
    if sorted(numberList) == numberList:
        return True
    else:
        return False

numberOfPasswords = 0

for number in passwordRange:
    numberString = str(number)
    if(check_double_digits(numberString)):
        if(check_never_decrease(numberString)):
            numberOfPasswords = numberOfPasswords + 1

print("There are " + str(numberOfPasswords) + " passwords within the input range")
