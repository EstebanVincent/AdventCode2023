import unittest
from day_1.solve import read_file, solve_part_1, solve_part_2


class Test_Day1(unittest.TestCase):
    def setUp(self):
        # Read the input files
        self.input_lines = read_file("day_1/input.txt")
        self.example_1_lines = read_file("day_1/example_1.txt")
        self.example_2_lines = read_file("day_1/example_2.txt")
        self.example_2_debug_lines = read_file("day_1/example_2_debug.txt")

    def test_solve_part_1_with_example_1(self):
        result = solve_part_1(self.example_1_lines)
        self.assertEqual(result, 142)

    def test_solve_part_1_with_input(self):
        result = solve_part_1(self.input_lines)
        self.assertEqual(result, 54239)

    def test_solve_part_2_with_example_2(self):
        result = solve_part_2(self.example_2_lines)
        self.assertEqual(result, 281)

    def test_solve_part_2_with_example_2_debug(self):
        result = solve_part_2(self.example_2_debug_lines)
        self.assertEqual(result, 363)

    def test_solve_part_2_with_input(self):
        result = solve_part_2(self.input_lines)
        self.assertEqual(result, 55343)


if __name__ == "__main__":
    unittest.main()
