import re
import sympy
import tokenize


# Exercise 1
str_input = input('Please enter any string in English:')
# Making from string a list of words (splitting)
str_split = str_input.split(' ')
counter = 0

for word in str_split:
    # Checking and counting for Vowels
    result = len(re.findall(r'aa|AA|ee|EE|ii|II|uu|UU|oo|OO', word))
    if result == 1:
        counter += 1
    else:
        pass
if counter == 1:
    print(f'This string contains {counter} word with double vowels in a row')
else:
    print(f'This string contains {counter} words with double vowels in a row')


# Exercise 2
dict_input = input('Please enter a dict in format {shop: price} :')

# Parsing dictionary from input
try:
    sympy_dict = sympy.parsing.sympy_parser.parse_expr(dict_input)
except tokenize.TokenError:
    print('Invalid dict, please enter a dict in format {shop: price}!')
except SyntaxError:
    print('It is not a dict! Please enter a dict in format {shop: price}!')
else:
    if type(sympy_dict) is dict:
        try:
            max_price = int(input('Please enter a max price (integer):'))
            min_price = int(input('Please enter a min price (integer):'))
        except ValueError:
            print('Invalid max and min prices, please enter an integers')
        else:
            # Getting keys and values from dictionary
            key_list = list(sympy_dict.keys())
            val_list = list(sympy_dict.values())
            output_list = list()
            for value in val_list:
                # Checking is shop accepting criteria
                if max_price > value > min_price:
                    index = val_list.index(value)
                    shop_name = key_list[index]
                    output_list.append(shop_name)
                else:
                    pass
            if len(output_list) > 0:
                print(f'Those shops are accepting criteria: {output_list}')
            else:
                print('There are no shop that accepting criteria!!!')
    else:
        print('It is not a dict! Please enter a dict in format {shop: price}!')
