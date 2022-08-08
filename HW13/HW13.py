from datetime import date

from request import Vacation
from request import SickLeave
from request import DayOff
from request import title_type


if __name__ == '__main__':
    vac_from_date = date(2022, 9, 10)
    vac_to_date = date(2022, 9, 29)
    vacation2 = Vacation('Bob', 'Marley', vac_from_date, vac_to_date)
    vacation2.title()
    vacation2.pattern()

    print('=============================================================')

    sick_from_date = date(2022, 6, 3)
    sick_to_date = date(2022, 7, 1)
    vacation2 = SickLeave('Steve', 'Jobes', sick_from_date, sick_to_date)
    vacation2.title()
    vacation2.pattern()

    print('=============================================================')

    day_from_date = date(2022, 9, 1)
    day_to_date = date(2022, 9, 3)
    vacation2 = DayOff('Bill', 'Gates', day_from_date, day_to_date)
    vacation2.title()
    vacation2.pattern()




