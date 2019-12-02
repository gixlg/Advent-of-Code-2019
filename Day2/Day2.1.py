f = open("inputDay2.txt", "r")
line = f.readline()
print(line)
instructions = line.split(",")
instructions = list(map(int, instructions))
print(instructions)
# replace position 1 with the value 12 and replace position 2 with the value 2.
instructions[1] = 12
instructions[2] = 2
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
    print(instructions)
    index += 4
print("Output is :" + str(instructions[0]))