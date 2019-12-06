from Day5.Operation import Operation


class Program:
    def __init__(self, program, program_input=None):
        print(program)
        self.instructions = program.split(",")
        self.instructions = list(map(int, self.instructions))
        self.outputs = []
        self.program_input = program_input
        self.index = 0

    def execute_program(self):
        print(self.instructions)
        program_is_running = True
        while program_is_running:
            operation = Operation(self.instructions[self.index])
            program_is_running = self.execute_operation(operation)
            print(self.instructions)
            
    def execute_operation(self, operation):
        if operation.opcode == 1:  # Add
            input1 = self.instructions[self.index + 1]
            input2 = self.instructions[self.index + 2]
            parameter1 = self.instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = self.instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            output_value = parameter1 + parameter2
            if operation.mode_of_3rd_parameter == "immediate mode":
                raise ValueError('3rd parameter is in immediate mode')
            output_position = self.instructions[self.index + 3]
            self.instructions[output_position] = output_value
            self.index += 4
        elif operation.opcode == 2:  # Multiplication
            input1 = self.instructions[self.index + 1]
            input2 = self.instructions[self.index + 2]
            parameter1 = self.instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = self.instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            output_value = parameter1 * parameter2
            if operation.mode_of_3rd_parameter == "immediate mode":
                raise ValueError('3rd parameter is in immediate mode')
            output_position = self.instructions[self.index + 3]
            self.instructions[output_position] = output_value
            self.index += 4
        elif operation.opcode == 3:  # Read
            input1 = self.instructions[self.index + 1]
            input_value_from_user = self.program_input
            self.instructions[input1] = int(
                input("Provide an input: ")) if self.program_input is None else input_value_from_user
            self.index += 2
        elif operation.opcode == 4:  # Write
            input1 = self.instructions[self.index + 1]
            output = self.instructions[input1];
            self.outputs.append(output)
            print(f"OUTPUT: {output}")
            self.index += 2
        elif operation.opcode == 99:
            print(f"Hit the End opcode")
            return False
        return True


if __name__ == '__main__':
    with open("inputDay5.txt", "r") as f:
        line = f.readline()
        program = Program(line)
        program.execute_program()

