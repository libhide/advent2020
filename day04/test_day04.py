import unittest
from day04 import create_list_of_passports
from day04 import is_valid_passport
from day04 import get_passport_data
from day04 import is_birth_year_valid
from day04 import is_issue_year_valid
from day04 import is_expiration_year_valid
from day04 import is_height_valid
from day04 import is_hair_color_valid
from day04 import is_eye_color_valid
from day04 import is_passport_id_valid
from day04 import is_passport_data_valid


class Day04Test(unittest.TestCase):
    def test_create_list_of_passports(self):
        data = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm\n\niyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929\n\nhcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm\n\nhcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in"
        self.assertEqual(len(create_list_of_passports(data)), 4)

    def test_is_passport_valid(self):
        passport1 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm"
        passport2 = (
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929"
        )
        passport3 = (
            "hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm"
        )
        passport4 = "hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in"
        self.assertEqual(is_valid_passport(passport1), True)
        self.assertEqual(is_valid_passport(passport2), False)
        self.assertEqual(is_valid_passport(passport3), True)
        self.assertEqual(is_valid_passport(passport4), False)

    def test_get_passport_data(self):
        passport1 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm"
        passport2 = (
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929"
        )

        passport1_data = {
            "byr": "1937",
            "iyr": "2017",
            "eyr": "2020",
            "hgt": "183cm",
            "hcl": "#fffffd",
            "ecl": "gry",
            "pid": "860033327",
        }

        passport2_data = {
            "byr": "1929",
            "iyr": "2013",
            "eyr": "2023",
            "hgt": "",
            "hcl": "#cfa07d",
            "ecl": "amb",
            "pid": "028048884",
        }

        self.assertEqual(get_passport_data(passport1), passport1_data)

        self.assertEqual(get_passport_data(passport2), passport2_data)

    def test_is_birth_year_valid(self):
        y1 = "2002"
        y2 = "2003"
        self.assertEqual(is_birth_year_valid(y1), True)
        self.assertEqual(is_birth_year_valid(y2), False)

    def test_is_issue_year_valid(self):
        y1 = "2012"
        y2 = "2020"
        y3 = "1920"
        self.assertEqual(is_issue_year_valid(y1), True)
        self.assertEqual(is_issue_year_valid(y2), True)
        self.assertEqual(is_issue_year_valid(y3), False)

    def test_is_expiration_year_valid(self):
        y1 = "2012"
        y2 = "2020"
        y3 = "2025"
        self.assertEqual(is_expiration_year_valid(y1), False)
        self.assertEqual(is_expiration_year_valid(y2), True)
        self.assertEqual(is_expiration_year_valid(y3), True)

    def test_is_height_valid(self):
        h1 = "60in"
        h2 = "190cm"
        h3 = "190in"
        h4 = "190"
        self.assertEqual(is_height_valid(h1), True)
        self.assertEqual(is_height_valid(h2), True)
        self.assertEqual(is_height_valid(h3), False)
        self.assertEqual(is_height_valid(h4), False)

    def test_is_hair_color_valid(self):
        hex1 = "#123abc"
        hex2 = "#123abz"
        hex3 = "123abc"
        self.assertEqual(is_hair_color_valid(hex1), True)
        self.assertEqual(is_hair_color_valid(hex2), False)
        self.assertEqual(is_hair_color_valid(hex3), False)

    def test_is_eye_color_valid(self):
        color1 = "brn"
        color2 = "wat"
        self.assertEqual(is_eye_color_valid(color1), True)
        self.assertEqual(is_eye_color_valid(color2), False)

    def test_is_passport_id_valid(self):
        pid1 = "000000001"
        pid2 = "0123456789"
        self.assertEqual(is_passport_id_valid(pid1), True)
        self.assertEqual(is_passport_id_valid(pid2), False)

    def test_is_passport_data_valid(self):
        passport1_data = {
            "byr": "1937",
            "iyr": "2017",
            "eyr": "2020",
            "hgt": "183cm",
            "hcl": "#fffffd",
            "ecl": "gry",
            "pid": "860033327",
        }

        passport2_data = {
            "byr": "1929",
            "iyr": "2013",
            "eyr": "2023",
            "hgt": "",
            "hcl": "#cfa07d",
            "ecl": "amb",
            "pid": "028048884",
        }

        self.assertEqual(is_passport_data_valid(passport1_data), True)
        self.assertEqual(is_passport_data_valid(passport2_data), False)


if __name__ == "__main__":
    unittest.main()
