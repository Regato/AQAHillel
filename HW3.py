import re
import sympy
import simplejson


# Exercise 1
word_input = input('Please enter a one string word:')
word_len = len(word_input)
symbol_list = []

# Check is string a one correct word or not
if any(not symbol_check.isalpha() for symbol_check in word_input):
    print('Invalid word, please enter a one string word!')
else:
    for symbol in word_input:
        symbol_list.append(symbol)

# Try is number integer or not
try:
    number_input = sympy.parsing.sympy_parser.parse_expr(input('Please enter an integer number:'))
    isinstance(number_input, int)
except:
    print('Invalid number, please enter an integer number!')
else:
    if 0 < number_input <= word_len:
        output_symbol = symbol_list[number_input-1]
        print(f'The {number_input} symbol in {word_input} is {output_symbol}')
    elif number_input == 0 or number_input < 0:
        print('You can\'t use zero or negative numbers!')
    else:
        print(f'Invalid number, word lenght is {word_len}, but you entered {number_input}')


# Exercise 2
string_input = input('Please enter any string of word/words:')
word_counter = len((re.findall(r'\w+', string_input)))

# Check is string a one correct word or not
if any(not symbol_check.isalpha() and not symbol_check.isspace() for symbol_check in string_input):
    print('Invalid string, please enter any string of word/words!')
elif word_counter == 1:
    print(f'The string contains {word_counter} word!')
else:
    print(f'The string contains {word_counter} words!')


# Exercise 3
input_list = input('Please enter a list with any data:')
unpacked_list = []
number_list = []

# Check is list entered correctly
try:
    sympy_list = sympy.parsing.sympy_parser.parse_expr(input_list)
    isinstance(sympy_list, list)
except:
    print('Invalid list, please enter a list with any data!')
else:
    # Unpacking all included lists in list
    for index in input_list:
        if isinstance(index, list):
            list_counter = str(index).count('[')
            string_value = str(index)
            unpack_value = '[' + string_value[list_counter: -list_counter: 1] + ']'
            json_unpack = simplejson.loads(unpack_value)
            unpacked_list += json_unpack
        else:
            unpacked_list.append(index)
    # Check all values in list for numbers
    for value in unpacked_list:
        if isinstance(value, int) or isinstance(value, float):
            number_list.append(value)
        elif isinstance(value, str):
            if value.isnumeric():
                value = sympy.parsing.sympy_parser.parse_expr(value)
                number_list.append(value)
            else:
                pass
        else:
            pass
    if len(number_list) > 0:
        print(f'Numbers list is: {number_list}')
    else:
        print(f'Numbers list is empty!')
