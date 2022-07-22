import sympy
from tokenize import TokenError
from first_function import input_argument
from second_function import output_collection


try:
    any_int = int(input('Please enter an Integer number:'))
except ValueError:
    print('Invalid argument, please enter an Integer!')
else:
    try:
        any_list = input('Please enter a list of numbers:')
        sympy_value = sympy.parsing.sympy_parser.parse_expr(any_list)
    except TokenError:
        output_message = 'Invalid list, please enter it again'

        print(output_message)
    except SyntaxError:
        output_message = 'It is not a list, please enter a list!!!'

        print(output_message)
    else:
        arg_value = input_argument(any_int)
        collection = output_collection(sympy_value, arg_value)
        print(f'Output collection is {collection}')
