from Day5.Operation import Operation


def execute_program(program, input_from_user):
    print(program)
    instructions = program.split(",")
    instructions = list(map(int, instructions))
    print(instructions)
    index = 0
    while True:
        operation = Operation(instructions[index])
        if operation.opcode == 1: #Add
            input1 = instructions[index + 1]
            input2 = instructions[index + 2]
            parameter1 = instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            output_value = parameter1 + parameter2
            if operation.mode_of_3rd_parameter == "immediate mode":
                raise ValueError('3rd parameter is in immediate mode')
            output_position = instructions[index + 3]
            instructions[output_position] = output_value
            index += 4
        elif operation.opcode == 2: #Multiplication
            input1 = instructions[index + 1]
            input2 = instructions[index + 2]
            parameter1 = instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            output_value = parameter1 * parameter2
            if operation.mode_of_3rd_parameter == "immediate mode":
                raise ValueError('3rd parameter is in immediate mode')
            output_position = instructions[index + 3]
            instructions[output_position] = output_value
            index += 4
        elif operation.opcode == 3: #Read
            input1 = instructions[index + 1]
            input_value_from_user = int(input_from_user)
            instructions[input1] = input_value_from_user
            index += 2
        elif operation.opcode == 4: #Write
            input1 = instructions[index + 1]
            parameter1 = instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            print(f"OUTPUT: {parameter1}")
            index += 2
        elif operation.opcode == 5: #jump-if-true
            input1 = instructions[index + 1]
            input2 = instructions[index + 2]
            parameter1 = instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            if parameter1 != 0:
                index = parameter2
            else:
                index += 3
        elif operation.opcode == 6: #jump-if-false
            input1 = instructions[index + 1]
            input2 = instructions[index + 2]
            parameter1 = instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            if parameter1 == 0:
                index = parameter2
            else:
                index += 3
        elif operation.opcode == 7: #less than
            input1 = instructions[index + 1]
            input2 = instructions[index + 2]
            input3 = instructions[index + 3]
            parameter1 = instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            parameter3 = input3

            if parameter1 < parameter2:
                instructions[parameter3] = 1
            else:
                instructions[parameter3] = 0
            index += 4
        elif operation.opcode == 8: #equals
            input1 = instructions[index + 1]
            input2 = instructions[index + 2]
            input3 = instructions[index + 3]
            parameter1 = instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            parameter3 = input3

            if parameter1 == parameter2:
                instructions[parameter3] = 1
            else:
                instructions[parameter3] = 0
            index += 4

        elif operation.opcode == 99:
            print(f"Hit the End opcode")
            break

        print(instructions)



with open("inputDay5.txt", "r") as f:
    line = f.readline()
    execute_program(line, 5)

#3,9,8,9,10,9,4,9,99,-1,8 -
#Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
#execute_program("3,9,8,9,10,9,4,9,99,-1,8")

#3,9,7,9,10,9,4,9,99,-1,8 -
#Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
#execute_program("3,9,7,9,10,9,4,9,99,-1,8")

#3,3,1108,-1,8,3,4,3,99 -
#Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
#execute_program("3,3,1108,-1,8,3,4,3,99")

#3,3,1107,-1,8,3,4,3,99 -
#Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
#execute_program("3,3,1107,-1,8,3,4,3,99")

#Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
#3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
#3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
#execute_program("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
#execute_program("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")

#execute_program("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
#The above example program uses an input instruction to ask for a single number.
#The program will then output 999 if the input value is below 8,
#output 1000 if the input value is equal to 8,
#or output 1001 if the input value is greater than 8.



