import string
import random
from random import randint
from datetime import date
from unittest import TestCase

from request import Vacation
from request import SickLeave
from request import DayOff


# Returns random number in range from first to last
def random_number(first: int, last: int) -> int:
    """Random number function in diapason

        Args:
            first(int): any integer argument
            last(int): any integer argument that > than first argument

        Returns:
            random number
    """
    number_output = randint(first, last)

    return number_output


# Returns random string with lower and UPPER cases
def random_any_string(iteration: int) -> int:
    """Random string of letters function

        Args:
            iteration(int): any integer argument

        Returns:
            random string of letters (upper case +/or lower case)
    """
    letters = string.ascii_letters
    string_output = ''.join(random.choice(letters) for index in range(iteration))

    return string_output


class VacationTest(TestCase):
    # Making random data
    random_value1 = random_number(1, 9)
    random_value2 = random_number(1, 9)
    random_value3 = random_number(1, 9)
    random_value4 = random_number(1, 9)
    random_name = random_any_string(11)
    random_surname = random_any_string(11)

    def setUp(self) -> None:
        self.vac_from_date = date(2022, self.random_value1, self.random_value2)
        self.vac_to_date = date(2022, self.random_value3, self.random_value4)
        self.vacation = Vacation(self.random_name,
                                 self.random_surname,
                                 self.vac_from_date,
                                 self.vac_to_date
                                 )

    def test_first_name(self):
        self.assertEqual(self.vacation.first_name, self.random_name)

    def test_last_name(self):
        self.assertEqual(self.vacation.last_name, self.random_surname)

    def test_from_date(self):
        self.assertEqual(self.vacation.from_date, self.vac_from_date)

    def test_to_date(self):
        self.assertEqual(self.vacation.to_date, self.vac_to_date)

    def test_title(self):
        title_type = type(self.vacation.title())
        title_type_str = str(title_type)
        self.assertEqual(title_type_str, "<class 'NoneType'>")

    def test_pattern(self):
        title_type = type(self.vacation.pattern())
        title_type_str = str(title_type)
        self.assertEqual(title_type_str, "<class 'NoneType'>")


class SickLeaveTest(TestCase):
    # Making random data
    random_value1 = random_number(1, 9)
    random_value2 = random_number(1, 9)
    random_value3 = random_number(1, 9)
    random_value4 = random_number(1, 9)
    random_name = random_any_string(11)
    random_surname = random_any_string(11)

    def setUp(self) -> None:
        self.sick_from_date = date(2022, self.random_value1, self.random_value2)
        self.sick_to_date = date(2022, self.random_value3, self.random_value4)
        self.sick_leave = SickLeave(self.random_name,
                                    self.random_surname,
                                    self.sick_from_date,
                                    self.sick_to_date
                                    )

    def test_first_name(self):
        self.assertEqual(self.sick_leave.first_name, self.random_name)

    def test_last_name(self):
        self.assertEqual(self.sick_leave.last_name, self.random_surname)

    def test_from_date(self):
        self.assertEqual(self.sick_leave.from_date, self.sick_from_date)

    def test_to_date(self):
        self.assertEqual(self.sick_leave.to_date, self.sick_to_date)

    def test_title(self):
        title_type = type(self.sick_leave.title())
        title_type_str = str(title_type)
        self.assertEqual(title_type_str, "<class 'NoneType'>")

    def test_pattern(self):
        title_type = type(self.sick_leave.pattern())
        title_type_str = str(title_type)
        self.assertEqual(title_type_str, "<class 'NoneType'>")


class DayOffTest(TestCase):
    # Making random data
    random_value1 = random_number(1, 9)
    random_value2 = random_number(1, 9)
    random_value3 = random_number(1, 9)
    random_value4 = random_number(1, 9)
    random_name = random_any_string(11)
    random_surname = random_any_string(11)

    def setUp(self) -> None:
        self.day_from_date = date(2022, self.random_value1, self.random_value2)
        self.day_to_date = date(2022, self.random_value3, self.random_value4)
        self.day_of = DayOff(self.random_name,
                             self.random_surname,
                             self.day_from_date,
                             self.day_to_date
                             )

    def test_first_name(self):
        self.assertEqual(self.day_of.first_name, self.random_name)

    def test_last_name(self):
        self.assertEqual(self.day_of.last_name, self.random_surname)

    def test_from_date(self):
        self.assertEqual(self.day_of.from_date, self.day_from_date)

    def test_to_date(self):
        self.assertEqual(self.day_of.to_date, self.day_to_date)

    def test_title(self):
        title_type = type(self.day_of.title())
        title_type_str = str(title_type)
        self.assertEqual(title_type_str, "<class 'NoneType'>")

    def test_pattern(self):
        title_type = type(self.day_of.pattern())
        title_type_str = str(title_type)
        self.assertEqual(title_type_str, "<class 'NoneType'>")
