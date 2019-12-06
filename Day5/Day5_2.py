from Day5.Day5_1 import Program


class ProgramV2(Program):
    def execute_operation(self, operation):
        programm_is_running = Program.execute_operation(self, operation)
        if operation.opcode == 5: #jump-if-true
            input1 = self.instructions[self.index + 1]
            input2 = self.instructions[self.index + 2]
            parameter1 = self.instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = self.instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            if parameter1 != 0:
                self.index = parameter2
            else:
                self.index += 3
        elif operation.opcode == 6: #jump-if-false
            input1 = self.instructions[self.index + 1]
            input2 = self.instructions[self.index + 2]
            parameter1 = self.instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = self.instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            if parameter1 == 0:
                self.index = parameter2
            else:
                self.index += 3
        elif operation.opcode == 7: #less than
            input1 = self.instructions[self.index + 1]
            input2 = self.instructions[self.index + 2]
            input3 = self.instructions[self.index + 3]
            parameter1 = self.instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = self.instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            parameter3 = input3

            if parameter1 < parameter2:
                self.instructions[parameter3] = 1
            else:
                self.instructions[parameter3] = 0
            self.index += 4
        elif operation.opcode == 8: #equals
            input1 = self.instructions[self.index + 1]
            input2 = self.instructions[self.index + 2]
            input3 = self.instructions[self.index + 3]
            parameter1 = self.instructions[input1] if operation.mode_of_1st_parameter == "position mode" else input1
            parameter2 = self.instructions[input2] if operation.mode_of_2nd_parameter == "position mode" else input2
            parameter3 = input3

            if parameter1 == parameter2:
                self.instructions[parameter3] = 1
            else:
                self.instructions[parameter3] = 0
            self.index += 4
        return programm_is_running

if __name__ == '__main__':
    with open("inputDay5.txt", "r") as f:
        line = f.readline()
        program = ProgramV2(line, 5)
        program.execute_program()




