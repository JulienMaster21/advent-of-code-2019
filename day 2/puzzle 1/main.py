# Get input
program_input = open("input.txt", "r")

# Split input into list
program = program_input.read().split(",")

# Initialise instructions list
instructions = []

# Fill instructions list
for number in range(0, len(program), 4):
    if int(program[number]) == 99:
        break
    else:
        instructions.append({
            "OPCode": int(program[number]),
            "value1": int(program[number + 1]),
            "value2": int(program[number + 2]),
            "outputAddress": int(program[number + 3])
        })

# Re-create 1202 error
program[1] = '12'
program[2] = '2'

# Loop through the instructions
for instruction in instructions:
    if instruction["OPCode"] == 1:
        program[instruction["outputAddress"]] = str(int(program[instruction["value1"]]) +
                                                    int(program[instruction["value2"]]))
    elif instruction["OPCode"] == 2:
        program[instruction["outputAddress"]] = str(int(program[instruction["value1"]]) *
                                                    int(program[instruction["value2"]]))
    else:
        print("Not a valid OPCode")

# Print answer
print(program[0])
