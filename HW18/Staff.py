from abc import ABC
from abc import abstractmethod
from collections import namedtuple as nt
from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar


class SexEnum(Enum):
    MEN = "Men"
    WOMEN = "Women"


@dataclass
class Human(ABC):
    """Takes first_name, last_name, age"""
    human_list: ClassVar[list] = list()
    first_name: str = field(compare=True)
    last_name: str = field(compare=True)
    age: int = field(compare=True)

    def __post_init__(self):
        self.__class__.print_new_human(self)
        self.__class__.add_human_list(self)

    @abstractmethod
    def new_human(self, position):
        pass

    @abstractmethod
    def print_new_human(self):
        pass

    @abstractmethod
    def add_human_list(self):
        pass

    @abstractmethod
    def print_human_list(self):
        pass


New_Director = nt('New_Director', ('first_name', 'last_name', 'age', 'position',  'sex'))


@dataclass
class Director(Human):
    """Takes sex attribute (ENUM field)"""
    sex: SexEnum
    position: str = field(default=None)

    def print_sex(self):
        print(self.sex.value)

    def new_human(self, position='Director'):
        # Returns named tuple
        self.position = position

        return New_Director(self.first_name,
                            self.last_name,
                            self.age,
                            self.position,
                            self.sex.value
                            )

    def print_new_human(self):
        print(f'New Director {self.first_name} {self.last_name} was hired.')

    def add_human_list(self):
        # Add director to a human list
        director = nt('Director', ('first_name', 'last_name', 'sex'))
        self.__class__.human_list.append(director(self.first_name, self.last_name, self.sex.value))

    def print_human_list(self):
        print(self.__class__.human_list)

    def __del__(self):
        pass


New_Head_Teacher = nt('New_Head_Teacher', ('first_name', 'last_name', 'age', 'position', 'sex'))


@dataclass
class HeadTeacher(Human):
    sex: SexEnum
    position: str = field(default=None)

    def print_sex(self):
        print(self.sex.value)

    def new_human(self, position='HeadTeacher'):
        # Returns named tuple
        self.position = position

        return New_Head_Teacher(self.first_name,
                                self.last_name,
                                self.age,
                                self.position,
                                self.sex.value
                                )

    def print_new_human(self):
        print(f'New HeadTeacher {self.first_name} {self.last_name} was hired.')

    def add_human_list(self):
        # Add director to a human list
        head_teacher = nt('HeadTeacher', ('first_name', 'last_name', 'sex'))
        self.__class__.human_list.append(head_teacher(self.first_name, self.last_name, self.sex.value))

    def print_human_list(self):
        print(self.__class__.human_list)

    def __del__(self):
        pass


New_Teacher = nt('New_Teacher', ('first_name', 'last_name', 'age', 'position', 'sex'))


@dataclass
class Teacher(Human):
    sex: SexEnum
    position: str = field(default=None)

    def print_sex(self):
        print(self.sex.value)

    def new_human(self, position='Teacher'):
        # Returns named tuple
        self.position = position

        return New_Teacher(self.first_name,
                           self.last_name,
                           self.age,
                           self.position,
                           self.sex.value
                           )

    def print_new_human(self):
        print(f'New Teacher {self.first_name} {self.last_name} was hired.')

    def add_human_list(self):
        # Add director to a human list
        teacher = nt('Teacher', ('first_name', 'last_name', 'sex'))
        self.__class__.human_list.append(teacher(self.first_name, self.last_name, self.sex.value))

    def print_human_list(self):
        print(self.__class__.human_list)

    def __del__(self):
        pass


New_Student = nt('New_Teacher', ('first_name', 'last_name', 'age', 'position', 'sex'))


@dataclass
class Student(Human):
    sex: SexEnum
    position: str = field(default=None, compare=True)

    def print_sex(self):
        print(self.sex.value)

    def new_human(self, position='Student'):
        # Returns named tuple
        self.position = position

        return New_Student(self.first_name,
                           self.last_name,
                           self.age,
                           self.position,
                           self.sex.value
                           )

    def print_new_human(self):
        print(f'New Student {self.first_name} {self.last_name} was hired.')

    def add_human_list(self):
        # Add director to a human list
        student = nt('Student', ('first_name', 'last_name', 'sex'))
        self.__class__.human_list.append(student(self.first_name, self.last_name, self.sex.value))

    def print_human_list(self):
        print(self.__class__.human_list)

    def __del__(self):
        pass
