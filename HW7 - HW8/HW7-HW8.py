from sympy import Integer
from sympy import Symbol

from cinema import make_input
from cinema import cinema_age
from cinema import parse_value
from cinema import restart_program


input_value = make_input()
parse_input = parse_value(input_value)
parse_type_int = isinstance(parse_input, Integer)
parse_type_str = isinstance(parse_input, Symbol)


if parse_type_int or parse_type_str:
    if cinema_age(parse_input) is None:
        restart = restart_program()

    else:
        output = cinema_age(parse_input)
        print(output)

else:
    print(parse_input)
    restart = restart_program()
