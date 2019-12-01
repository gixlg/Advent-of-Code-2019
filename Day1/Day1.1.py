import math

f = open("inputDay1.txt", "r")
masses = list(f)
total_required_fuel = 0
for mass in masses:
    required_fuel = math.floor(int(mass) / 3) - 2
    print("required fuel:", required_fuel)
    total_required_fuel += required_fuel
print("total required fuel: " + str(total_required_fuel))