import unittest
from Day5.Day5_2 import ProgramV2


class MyTestCase(unittest.TestCase):
    def test_input_equal_to_8(self):
        program = ProgramV2("3,9,8,9,10,9,4,9,99,-1,8", 8)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 1)

    def test_input_not_equal_to_8(self):
        program = ProgramV2("3,9,8,9,10,9,4,9,99,-1,8", 7)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 0)

    def test_input_less_than_8(self):
        program = ProgramV2("3,9,7,9,10,9,4,9,99,-1,8", 7)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 1)

    def test_input_not_less_than_8(self):
        program = ProgramV2("3,9,7,9,10,9,4,9,99,-1,8", 9)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 0)

    def test_input_equal_to_8_immediate_mode(self):
        program = ProgramV2("3,3,1108,-1,8,3,4,3,99", 8)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 1)

    def test_input_not_equal_to_8_immediate_mode(self):
        program = ProgramV2("3,3,1108,-1,8,3,4,3,99", 7)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 0)

    def test_input_less_than_8_immediate_mode(self):
        program = ProgramV2("3,3,1107,-1,8,3,4,3,99", 7)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 1)

    def test_input_not_less_than_8_immediate_mode(self):
        program = ProgramV2("3,3,1107,-1,8,3,4,3,99", 9)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 0)

    def test_output_0_if_the_input_is_zero(self):
        program = ProgramV2("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", 0)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 0)

    def test_output_1_if_the_input_is_not_zero(self):
        program = ProgramV2("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", 99)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 1)

    def test_output_0_if_the_input_is_zero_immediate_mode(self):
        program = ProgramV2("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", 0)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 0)

    def test_output_1_if_the_input_is_not_zero_immediate_mode(self):
        program = ProgramV2("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", 99)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 1)

    def test_output_999_if_the_input_value_is_below_8(self):
        program = ProgramV2("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", 7)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 999)

    def test_output_999_if_the_input_value_is_below_8(self):
        program = ProgramV2("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", 8)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 1000)

    def test_output_999_if_the_input_value_is_below_8(self):
        program = ProgramV2("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", 9)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 1001)


if __name__ == '__main__':
    unittest.main()
