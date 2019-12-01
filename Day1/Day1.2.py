import math


def compute_required_fuel(mass):
    total_required_fuel = 0
    required_fuel = math.floor(mass / 3) - 2
    while required_fuel != 0:
        total_required_fuel = total_required_fuel + required_fuel
        required_fuel = max(math.floor(required_fuel / 3) - 2, 0)
    return total_required_fuel



f = open("inputDay1.txt", "r")
masses = list(f)
total_required_fuel = 0
for mass in masses:
    required_fuel = compute_required_fuel(int(mass))
    print("required fuel:", required_fuel)
    total_required_fuel += required_fuel
print("total required fuel: " + str(total_required_fuel))
