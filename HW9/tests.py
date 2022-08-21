import datetime
import string
import unittest
import random
from random import randint
from unittest import TestCase

from HW9 import Human


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


class HumanTest(TestCase):
    # Making random data
    random_name = random_any_string(11)
    random_surname = random_any_string(11)
    sex = ['men', 'women']
    random_sex_ind = random_number(0, 1)
    random_age = random_number(18, 65)
    birth_date = datetime.date(1996, 8, 10)
    random_food = random_any_string(10)
    random_sentence = random_any_string(22)

    def test_population1(self):
        random_human1 = Human(self.random_name,
                             self.random_surname,
                             self.random_age,
                             self.sex[self.random_sex_ind]
                             )

        result = random_human1.population

        self.assertEqual(result, 1)

        del random_human1

    def test_population2(self):
        random_human2 = Human(self.random_name,
                             self.random_surname,
                             self.random_age,
                             self.sex[self.random_sex_ind]
                             )

        random_human2.population = 2
        result = random_human2.population

        self.assertEqual(result, 2)

        del random_human2

    def test_population3(self):
        random_human3 = Human(self.random_name,
                             self.random_surname,
                             self.random_age,
                             self.sex[self.random_sex_ind]
                             )

        random_human3.count_population()
        result = random_human3.population

        self.assertEqual(result, 2)

        del random_human3

    def test_population4(self):
        random_human4 = Human(self.random_name,
                             self.random_surname,
                             self.random_age,
                             self.sex[self.random_sex_ind]
                             )

        random_human4.__class__.count_population(5)
        result = random_human4.population

        self.assertEqual(result, 6)

        del random_human4

    def test_birth_date(self):
        random_human5 = Human(self.random_name,
                             self.random_surname,
                             self.random_age,
                             self.sex[self.random_sex_ind]
                             )

        random_human5.enter_birth_date(self.birth_date)

        self.assertEqual(random_human5.age, 25)

        del random_human5

    def test_eat(self):
        random_human6 = Human(self.random_name,
                             self.random_surname,
                             self.random_age,
                             self.sex[self.random_sex_ind]
                             )

        result = random_human6.eat(self.random_food)
        output_str = f'{self.random_name} is eating {self.random_food}.'

        self.assertEqual(result, output_str)

        del random_human6

    def test_sleep(self):
        random_human7 = Human(self.random_name,
                             self.random_surname,
                             self.random_age,
                             self.sex[self.random_sex_ind]
                            )

        result = random_human7.sleep()
        output_str = f'{self.random_name} is sleeping  on the bed.'

        self.assertEqual(result, output_str)

        del random_human7

    def test_sleep(self):
        random_human8 = Human(self.random_name,
                                self.random_surname,
                                self.random_age,
                                self.sex[self.random_sex_ind]
                                )

        result = random_human8.speak(self.random_sentence)
        output_str = f'{self.random_name} says {self.random_sentence}'

        self.assertEqual(result, output_str)

        del random_human8

    def test_walk1(self):
        random_human9 = Human(self.random_name,
                              self.random_surname,
                              self.random_age,
                              self.sex[self.random_sex_ind]
                              )

        result = random_human9.walk()
        output_str = f'{self.random_name} is walking anywhere!'

        self.assertEqual(result, output_str)

        del random_human9

    def test_walk2(self):
        random_human10 = Human(self.random_name,
                               self.random_surname,
                               self.random_age,
                               self.sex[self.random_sex_ind]
                               )

        result = random_human10.walk(self.random_sentence)
        output_str = f'{self.random_name} walks to {self.random_sentence}'

        self.assertEqual(result, output_str)

        del random_human10

    def test_stay(self):
        random_human11 = Human(self.random_name,
                              self.random_surname,
                              self.random_age,
                              self.sex[self.random_sex_ind]
                              )

        result = random_human11.stay()
        output_str = f'{self.random_name} is staying.'

        self.assertEqual(result, output_str)

        del random_human11

    def test_lie(self):
        random_human12 = Human(self.random_name,
                              self.random_surname,
                              self.random_age,
                              self.sex[self.random_sex_ind]
                              )

        result = random_human12.lie()
        output_str = f'{self.random_name} lies.'

        self.assertEqual(result, output_str)

        del random_human12


if __name__ == '__main__':
    unittest.main()