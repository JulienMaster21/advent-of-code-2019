# Imports
import numpy as np


# Define Module class
class Module:

    def __init__(self, mass):
        self.mass = mass
        self.fuelRequirement = int


# Initialise the classes list
modules = []

# Retrieve the mass of modules from input.txt
moduleInput = open("input.txt", "r")

# Add all modules to the modules list
currentMass = 0
line = moduleInput.readline()
while line != "":
    currentMass = int(line)
    modules.append(Module(currentMass))
    line = moduleInput.readline()

# Calculate fuel requirement
currentFuelRequirement = 0
for module in modules:
    # Take the mass
    currentFuelRequirement = module.mass

    # Divide by 3
    currentFuelRequirement /= 3

    # Round down
    currentFuelRequirement = np.floor(currentFuelRequirement)

    # Subtract 2
    currentFuelRequirement -= 2

    # Turn to int
    currentFuelRequirement = int(currentFuelRequirement)

    # Assign fuel requirement
    module.fuelRequirement = currentFuelRequirement

    # Check for additional fuel requirement
    while np.floor(currentFuelRequirement / 3) - 2 > 0:
        currentFuelRequirement = int(np.floor(currentFuelRequirement / 3) - 2)
        module.fuelRequirement += currentFuelRequirement

# Get the sum of all the fuel requirements
totalFuelRequirement = 0
for module in modules:
    totalFuelRequirement += module.fuelRequirement

print(totalFuelRequirement)
