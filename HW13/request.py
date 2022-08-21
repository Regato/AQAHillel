from abc import ABC
from abc import abstractmethod


def title_type(func):
    """Takes function object, returns title_wrapper object"""

    def title_wrapper(*args):
        """Takes *args, prints output string, returns func(*args)"""

        output_string = 'CEO Red Bull Inc.\nMr. John Bigbull'
        func(print(output_string))

        return func(*args)

    return title_wrapper


class Request(ABC):
    """Takes first_name and last_name, got title method (with title_type decorator) and
        abstract method pattern"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @title_type
    def title(self):
        pass

    @abstractmethod
    def pattern(self):
        pass


def vacation_type(func):
    """Takes function object, returns vacation_wrapper object"""

    def vacation_wrapper(self):
        """Takes self, prints output string, returns func(self)"""

        output_string = f'Hi John,' \
                        f'\nI need the paid vacations {self.from_date} to {self.to_date}.' \
                        f'\n{self.first_name} {self.last_name}'

        func(print(output_string))

        return func(self)

    return vacation_wrapper


def sick_leave_type(func):
    """Takes function object, returns sick_leave_wrapper object"""

    def sick_leave_wrapper(self):
        """Takes self, prints output string, returns func(self)"""

        output_string = f'Hi John,\n' \
                        f'I need the paid sick leave {self.from_date} to {self.to_date}.\n' \
                        f'{self.first_name} {self.last_name}'

        func(print(output_string))

        return func(self)

    return sick_leave_wrapper


def day_off_type(func):
    """Takes function object, returns day_off_wrapper object"""

    def day_off_wrapper(self):
        """Takes self, prints output string, returns func(self)"""

        output_string = f'Hi John,\n' \
                        f'I need the paid vacations {self.from_date} to {self.to_date}.' \
                        f'\n{self.first_name} {self.last_name}'

        func(print(output_string))

        return func(self)

    return day_off_wrapper


class Vacation(Request):
    """Inheritance class from Request class, takes Request arguments and from_date, to_date
        got method pattern (with vacation_type decorator)"""

    def __init__(self, first_name, last_name, from_date, to_date):
        super().__init__(first_name, last_name)
        self.from_date = from_date
        self.to_date = to_date

    @vacation_type
    def pattern(self):
        pass


class SickLeave(Request):
    """Inheritance class from Request class, takes Request arguments and from_date, to_date
        got method pattern (with sick_leave_type decorator)"""

    def __init__(self, first_name, last_name, from_date, to_date):
        super().__init__(first_name, last_name)
        self.from_date = from_date
        self.to_date = to_date

    @sick_leave_type
    def pattern(self):
        pass


class DayOff(Request):
    """Inheritance class from Request class, takes Request arguments and from_date, to_date
        got method pattern (with day_off_type decorator)"""

    def __init__(self, first_name, last_name, from_date, to_date):
        super().__init__(first_name, last_name)
        self.from_date = from_date
        self.to_date = to_date

    @day_off_type
    def pattern(self):
        pass
