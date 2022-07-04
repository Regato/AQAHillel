import tokenize
import sympy
from sympy import Integer
from sympy import Float
from sympy import Symbol


# Exercise 1
input_value = input('Please enter an argument of any type in Python format:')


# Function to detect value (argument) type
def arg_type(value):
    value_type = type(value)

    return value_type

# Parsing argument from input
try:
    sympy_value = sympy.parsing.sympy_parser.parse_expr(input_value)
except tokenize.TokenError:
    print('Invalid argument, please enter an argument of any type in Python format!')
except SyntaxError:
    print('It is not an argument! please enter an argument of any type in Python format!')
else:
    complete_output = arg_type(sympy_value)
    print(f'Type of your value is: {complete_output}')


# Exercise 2
input_value = input('Please enter argument of any type in Python format:')


# Function to make from value to float or return float 0
def arg_float(value):
    try:
        float(value)
    except TypeError:
        output_value = float(0)

        return output_value
    else:
        output_value = float(value)

        return output_value


# Parsing argument from input
try:
    sympy_value = sympy.parsing.sympy_parser.parse_expr(input_value)
except tokenize.TokenError:
    print('Invalid argument, please enter an argument of any type in Python format!')
except SyntaxError:
    print('It is not an argument! please enter an argument of any type in Python format!')
else:
    complete_output = arg_float(sympy_value)
    if complete_output == float(0):
        print(f'Python cannot make float from this value, so we return: {complete_output}')
    else:
        print(f'Python successfully maid float from your value, it is: {complete_output}')


# Exercise 2
input_value1 = input('Please enter a 1st argument of any type in Python format:')
input_value2 = input('Please enter a 2nd argument of any type in Python format:')


# Final function with boolean and types
def two_arg(value1, value2):
    value_type1 = type(value1)
    value_type2 = type(value2)

    int_bool1 = isinstance(value1, Integer)
    float_bool1 = isinstance(value1, Float)
    int_bool2 = isinstance(value2, Integer)
    float_bool2 = isinstance(value2, Float)

    symbol_bool1 = isinstance(value1, Symbol)
    str_bool1 = isinstance(value_type1, str)
    symbol_bool2 = isinstance(value2, Symbol)
    str_bool2 = isinstance(value_type2, str)

    if (int_bool1 or float_bool1) and (int_bool2 or float_bool2):
        math_diff = value1 - value2

        return math_diff

    elif (str_bool1 or symbol_bool1) and (str_bool2 or symbol_bool2):
        str_concat = str(value1) + str(value2)

        return str_concat

    elif (str_bool1 or symbol_bool1) and not (str_bool2 or symbol_bool2):
        output_dict = {str(value1): value2}

        return output_dict

    else:
        output_tuple = (value1, value2)

        return output_tuple


# Parsing value (argument) from input
try:
    sympy_value1 = sympy.parsing.sympy_parser.parse_expr(input_value1)
    sympy_value2 = sympy.parsing.sympy_parser.parse_expr(input_value2)
except tokenize.TokenError:
    print('Invalid Python argument, please enter any argument in Python format!')
except SyntaxError:
    print('It is not a Python argument! Please enter any argument in Python format!!!')
else:
    print(f'Your output is: {two_arg(sympy_value1, sympy_value2)}')
