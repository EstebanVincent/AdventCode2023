import unittest
from day_4.solve import read_file, solve_part_1, solve_part_2


class Test_Day4(unittest.TestCase):
    def setUp(self):
        # Read the input files
        self.input_lines = read_file("day_4/input.txt")
        self.example_1_lines = read_file("day_4/example_1.txt")
        self.example_2_lines = self.read_file("day_4/example_2.txt")

    def read_file(self, file_path):
        with open(file_path, "r") as file:
            return file.readlines()

    def test_solve_part_1_with_example_1(self):
        result = solve_part_1(self.example_1_lines)
        self.assertEqual(result, 4361)

    def test_solve_part_1_with_input(self):
        result = solve_part_1(self.input_lines)
        self.assertEqual(result, 549908)

    def test_solve_part_2_with_example_2(self):
        result = solve_part_2(self.example_1_lines)
        self.assertEqual(result, 467835)

    def test_solve_part_2_with_input(self):
        result = solve_part_2(self.input_lines)
        self.assertEqual(result, 81166799)


if __name__ == "__main__":
    unittest.main()
