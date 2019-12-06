import unittest
from Day5.Day5_1 import Program


class MyTestCase(unittest.TestCase):
    def test1(self):
        program = Program("1002,4,3,4,33")
        program.execute_program()
        self.assertEqual(program.instructions[-1], 99)

    def test_return_in_output_the_value_got_in_input(self):
        program = Program("3, 0, 4, 0, 99", 999)
        program.execute_program()
        self.assertEqual(program.outputs[-1], 999)

    def test3(self):
        program = Program("1101, 100, -1, 4, 0")
        program.execute_program()
        self.assertEqual(program.instructions[-1], 99)


if __name__ == '__main__':
    unittest.main()
