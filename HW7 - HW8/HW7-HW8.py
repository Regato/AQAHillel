from cinema import make_input
from cinema import cinema_age
from cinema import parse_value
from cinema import restart_program


input_value = make_input()
parse_input = parse_value(input_value)
parse_type = type(parse_input)


if parse_type is str:
    print(parse_input)

    restart = restart_program()
else:
    output = cinema_age(parse_input)
    print(output)


