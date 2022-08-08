import os
import sys

from request import Vacation
from request import SickLeave
from request import DayOff

# Take an input (1 or 2 or 3)
select_input = input('Select one of these types:\n'
                     '1.Vacation\n'
                     '2.SickLeave\n'
                     '3.DayOff\n'
                     'Select your number (1, 2, 3):')

if select_input == '1':
    # Take an input data
    vac_first_name = input('Enter first name:')
    vac_last_name = input('Enter last name:')
    vac_from_date = input('Enter from date:')
    vac_to_date = input('Enter to date:')
    # Make an Vacation object
    vacation = Vacation(vac_first_name, vac_last_name, vac_from_date, vac_to_date)
    # Call methods
    vacation.title()
    vacation.pattern()
elif select_input == '2':
    # Take an input data
    sick_first_name = input('Enter first name:')
    sick_last_name = input('Enter last name:')
    sick_from_date = input('Enter from date:')
    sick_to_date = input('Enter to date:')
    # Make an SickLeave object
    sick_leave = SickLeave(sick_first_name, sick_last_name, sick_from_date, sick_to_date)
    # Call methods
    sick_leave.title()
    sick_leave.pattern()
elif select_input == '3':
    # Take an input data
    day_first_name = input('Enter first name:')
    day_last_name = input('Enter last name:')
    day_from_date = input('Enter from date:')
    day_to_date = input('Enter to date:')
    # Make an DayOff object
    day_off = DayOff(day_first_name, day_last_name, day_from_date, day_to_date)
    # Call methods
    day_off.title()
    day_off.pattern()
else:
    # If not 1 or 2 or 3 - restart a program
    os.execl(sys.executable, sys.executable, *sys.argv)