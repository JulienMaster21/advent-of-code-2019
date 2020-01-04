output = 0
noun = 0
verb = 0
target_value = 19690720
while output != target_value:
    # Get input
    program_input = open("input.txt", "r")

    # Split input into list
    program = program_input.read().split(",")

    # Initialise instructions list
    instructions = []

    # Fill instructions list
    for number in range(0, len(program), 4):
        if int(program[number]) == 99:
            instructions.append({
                "op_code": int(program[number])
            })
            break
        else:
            instructions.append({
                "op_code": int(program[number]),
                "param1": int(program[number + 1]),
                "param2": int(program[number + 2]),
                "output_address": int(program[number + 3])
            })

    # Input noun and verb
    program[1] = str(noun)
    program[2] = str(verb)

    # Loop through the instructions
    for instruction in instructions:
        if instruction["op_code"] == 1:
            program[instruction["output_address"]] = str(int(program[instruction["param1"]]) +
                                                         int(program[instruction["param2"]]))
        elif instruction["op_code"] == 2:
            program[instruction["output_address"]] = str(int(program[instruction["param1"]]) *
                                                         int(program[instruction["param2"]]))
        elif instruction["op_code"] == 99:
            break
        else:
            print("Not a valid operation code")

    # Set output
    output = int(program[0])

    # Increment noun and verb
    if output != target_value:
        if verb == 99:
            noun += 1
            verb = 0
        else:
            verb += 1

# Print answer
print(100 * noun + verb)
