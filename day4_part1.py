passwordRange = range(231832,767346)

def check_double_digits(number):
    numberString = str(number)
    for char in numberString:
        charIndex = numberString.index(char) 
        if charIndex == len(numberString) - 1:
            return False
        elif char == numberString[charIndex + 1]:
            return True

def check_never_decrease(number):
    numberString = str(number)
    numberList = []
    for char in numberString:
        numberList.append(int(char))
    if sorted(numberList) == numberList:
        return True
    else:
        return False

numberOfPasswords = 0

for number in passwordRange:
    if(check_double_digits(number)):
        if(check_never_decrease(number)):
            numberOfPasswords = numberOfPasswords + 1

print("There are " + str(numberOfPasswords) + " passwords within the input range")
