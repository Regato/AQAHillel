from random import randint
from unittest import TestCase

from HW10 import input_argument
from HW10 import output_collection


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


class TestListValue(TestCase):
    # Making random data
    random_value = random_number(2, 125)
    random_list = [random_number(2, 700) for index in range(random_number(1, 20))]

    def test_value_function(self):
        result = input_argument(self.random_value)
        check_result = self.random_value * 100

        self.assertEqual(result, check_result)

    def test_list_function(self):
        result_list = output_collection(self.random_list, input_argument)
        check_result = [input_argument(item) for item in self.random_list]

        self.assertEqual(result_list, check_result)
