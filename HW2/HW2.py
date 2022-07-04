user_age = input('Please enter your age as number:')
reversed_age = ''.join(reversed(user_age))
length_age = len(user_age)

try:
    user_age.isnumeric()
except False:
    raise ValueError('Please enter your age as number')
else:
    int_age = int(user_age)

if user_age == reversed_age and length_age > 1:
    print(f'What\'s the interesting age! Your age is {user_age}.')
elif int_age < 7:
    print(f'Where are your parents? Your age is {user_age}.')
elif int_age < 16:
    print(f'This film is for adults only! Your age is {user_age}.')
elif int_age > 65:
    print(f'Show your pension certificate! Your age is {user_age}.')
else:
    print(f'There are no tickets anymore! Your age is {user_age}.')
