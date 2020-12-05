import unittest
from day05 import find_row_for_boarding_pass, find_col_for_boarding_pass


class Day05Test(unittest.TestCase):
    def test_find_row_for_boarding_pass(self):
        boarding_pass = "FBFBBFFRLR"
        row = find_row_for_boarding_pass(boarding_pass)
        self.assertEqual(row, 44)

    def test_find_col_for_boarding_pass(self):
        boarding_pass = "FBFBBFFRLR"
        col = find_col_for_boarding_pass(boarding_pass)
        self.assertEqual(col, 5)


if __name__ == "__main__":
    unittest.main()
