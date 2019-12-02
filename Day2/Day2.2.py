def execute_program(instructions, noun, verb):
    instructions[1] = noun
    instructions[2] = verb
    index = 0
    while True:
        operation = instructions[index]
        input1 = instructions[index + 1]
        input2 = instructions[index + 2]
        output_position = instructions[index + 3]
        output_value = 0
        if operation == 1:
            output_value = instructions[input1] + instructions[input2]
        elif operation == 2:
            output_value = instructions[input1] * instructions[input2]
        elif operation == 99:
            break
        instructions[output_position] = output_value
        # print(instructions)
        index += 4
    return instructions[0]


def brute_force(output_searched):
    for noun in range(100):
        for verb in range(100):
            print("n " + str(noun) + " v " + str(verb))
            output = execute_program(instructions.copy(), noun, verb)
            print(f"output {output}")
            if output == output_searched:
                return 100 * noun + verb


f = open("inputDay2.txt", "r")
line = f.readline()
instructions = line.split(",")
instructions = list(map(int, instructions))
print(instructions)
brute_force(19690720)



