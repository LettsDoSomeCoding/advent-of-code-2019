import math
import sys

massList = [line.rstrip('\r\n') for line in open(sys.argv[1])]

def calculateFuel(mass):
    fuel = 0
    if (mass >= 9):
        fuel = (mass // 3) - 2

    if fuel > 0:
        fuelsFuel = calculateFuel(fuel)
        fuel = fuel + fuelsFuel
    
    return fuel

totalFuel = 0

for mass in massList:
    mass = float(mass)
    fuel = calculateFuel(mass)
    totalFuel = totalFuel + fuel

print("the fuel you require for all the modules is " + str(int(totalFuel)))