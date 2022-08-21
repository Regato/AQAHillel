import unittest
from unittest import TestCase
from unittest import mock
from unittest.mock import patch

import os
from sympy import Integer
from sympy import Symbol

from cinema import make_input
from cinema import cinema_age
from cinema import parse_value
from cinema import restart_program


class TestCinema(TestCase):

    def test_restart(self):
        os.execl = mock.MagicMock()
        restart_program()
        assert os.execl.called

    @patch('builtins.input', return_value='15')
    def test_digit_str(self, make_input):
        result = make_input()
        self.assertEqual(result, '15')

    @patch('builtins.input', return_value='hrhgiur')
    def test_text_str(self, make_input):
        result = make_input()
        self.assertEqual(result, 'hrhgiur')

    @patch('builtins.input', return_value='1')
    def test_parse_int(self, make_input):
        catch_input = make_input()
        parse_input = parse_value(catch_input)
        instance = isinstance(parse_input, Integer)
        self.assertEqual(instance, True)

    @patch('builtins.input', return_value='doijdwoiajd')
    def test_parse_str(self, make_input):
        catch_input = make_input()
        parse_input = parse_value(catch_input)
        parse_type = type(parse_input)
        self.assertEqual(parse_type, Symbol)

    @patch('builtins.input', return_value='1')
    def test_cinema1(self, make_input):
        catch_input = make_input()
        parse_input = parse_value(catch_input)
        cinema_output = cinema_age(parse_input)
        type_output = type(cinema_output)
        self.assertEqual(type_output, str)

    @patch('builtins.input', return_value='9')
    def test_cinema2(self, make_input):
        catch_input = make_input()
        parse_input = parse_value(catch_input)
        cinema_output = cinema_age(parse_input)
        type_output = type(cinema_output)
        self.assertEqual(type_output, str)

    @patch('builtins.input', return_value='67')
    def test_cinema3(self, make_input):
        catch_input = make_input()
        parse_input = parse_value(catch_input)
        cinema_output = cinema_age(parse_input)
        type_output = type(cinema_output)
        self.assertEqual(type_output, str)

    @patch('builtins.input', return_value='11')
    def test_cinema4(self, make_input):
        catch_input = make_input()
        parse_input = parse_value(catch_input)
        cinema_output = cinema_age(parse_input)
        type_output = type(cinema_output)
        self.assertEqual(type_output, str)

    @patch('builtins.input', return_value='111')
    def test_cinema5(self, make_input):
        catch_input = make_input()
        parse_input = parse_value(catch_input)
        cinema_output = cinema_age(parse_input)
        type_output = type(cinema_output)
        self.assertEqual(type_output, str)


if __name__ == '__main__':
    unittest.main()