import os
import sys
import tokenize
import sympy
from sympy import Integer


def input_value():
    """Cinema strict for user age

        Returns:
            Inputted value.
    """

    input_string = input('Please enter your age (Integer Number):')

    return input_value


def cinema_age(value):
    """Cinema strict for user age

        Args:
            value: Already parsed value (only sympy).

        Returns:
            Cinema response for every age.
    """

    int_bool = isinstance(value, Integer)

    str_value = str(value)
    str_reversed = ''.join(reversed(str_value))
    str_len = len(str_value)
    str_list = [item for item in str_value if item == str_value[-1]]
    list_len = len(str_list)

    # Check is value Integer or Float
    if int_bool and value >= 0:
        if value < 7 and not (str_value == str_reversed and str_len == list_len and str_len > 1):
            response_message = f'You are {value}! Where are your parents?'

            return response_message
        elif value < 16 and not (str_value == str_reversed and str_len == list_len and str_len > 1):
            response_message = f'You are only {value}, but this film is adults only!'

            return response_message
        elif value > 65 and not (str_value == str_reversed and str_len == list_len and str_len > 1):
            response_message = f'Are you {value}? Show your pension ID!'

            return response_message
        elif str_value == str_reversed and str_len == list_len and str_len > 1:
            response_message = f'Oh you are {value}! What\'s the interesting age!'

            return response_message
        else:
            response_message = f'Despite you are {value}, there are no tickets anymore!'

            return response_message
    else:
        print('It is not Integer! Please enter your age (Integer Number)!!!')
        os.execl(sys.executable, sys.executable, *sys.argv)


def parse_value(value: str) -> str:
    """Parse value using sympy library.

        Args:
          value: Any string value.

        Returns:
          Sympy parsed value or restart a program.

        Raises:
          tokenize.TokenError: If value can not be parsed.
          SyntaxError: If value has invalid syntax.
    """

    try:
        sympy_value = sympy.parsing.sympy_parser.parse_expr(input_value)
    except tokenize.TokenError:
        output_message = 'Invalid age, please enter your age (Integer Number)'

        return output_message

        # Restart a program
        os.execl(sys.executable, sys.executable, *sys.argv)
    except SyntaxError:
        output_message = 'It is not your age! Please enter your age (Integer Number)!!!'

        return output_message

        # Restart a program
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:

        return sympy_value
