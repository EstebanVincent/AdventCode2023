import unittest
from day_2.solve import read_file, solve_part_1, solve_part_2


class Test_Day2(unittest.TestCase):
    def setUp(self):
        # Read the input files
        self.input_df = read_file("day_2/input.txt")
        self.example_1_df = read_file("day_2/example_1.txt")
        self.example_2_df = self.read_file("day_2/example_2.txt")

    def read_file(self, file_path):
        with open(file_path, "r") as file:
            return file.readlines()

    def test_solve_part_1_with_example_1(self):
        result = solve_part_1(self.example_1_df, red=12, green=13, blue=14)
        self.assertEqual(result, 8)

    def test_solve_part_1_with_input(self):
        result = solve_part_1(self.input_df, red=12, green=13, blue=14)
        self.assertEqual(result, 2076)

    def test_solve_part_2_with_example_2(self):
        result = solve_part_2(self.example_1_df)
        self.assertEqual(result, 2286)

    def test_solve_part_2_with_input(self):
        result = solve_part_2(self.input_df)
        self.assertEqual(result, 70950)


if __name__ == "__main__":
    unittest.main()
