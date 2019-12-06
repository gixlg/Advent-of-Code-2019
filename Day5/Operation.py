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