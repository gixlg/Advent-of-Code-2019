class Operation:
    def __init__(self, operation):
        self.original_operation_code = operation
        self.get_operation_info(operation)

    def get_operation_info(self, operation):
        # ABCDE
        # 1002

        # DE - two-digit opcode,      02 == opcode 2
        # C - mode of 1st parameter,  0 == position mode
        # B - mode of 2nd parameter,  1 == immediate mode
        # A - mode of 3rd parameter,  0 == position mode,
        #                                  omitted due to being a leading zero
        operation = str(operation)
        operation = operation.rjust(5, "0")
        self.opcode=int(operation[3:5])
        self. mode_of_1st_parameter = self.get_mode(operation[2])
        self.mode_of_2nd_parameter = self.get_mode(operation[1])
        self.mode_of_3rd_parameter = self.get_mode(operation[0])

    def get_mode(self, mode):
        return "position mode" if mode == "0" else "immediate mode"


def execute_program(program):
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
            input_value_from_user = 1
            instructions[input1] = input_value_from_user
            index += 2
        elif operation.opcode == 4: #Write
            input1 = instructions[index + 1]
            print(f"OUTPUT: {instructions[input1]}")
            index += 2

        elif operation.opcode == 99:
            print(f"Hit the End opcode")
            break

        print(instructions)

with open("inputDay5.txt", "r") as f:
    #line = "1002,4,3,4,33"
    #line = "3, 0, 4, 0, 99"
    #line = "1101, 100, -1, 4, 0"
    line = f.readline()
    execute_program(line)

