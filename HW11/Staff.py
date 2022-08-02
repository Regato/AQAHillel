from abc import ABC
from abc import abstractmethod
from collections import namedtuple as nt


class Human(ABC):
    human_list = list()

    def __init__(self, first_name, last_name, age, position=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position
        self.__class__.print_new_human(self)
        self.__class__.add_human_list(self)

    @abstractmethod
    def new_human(self, value):
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


New_Director = nt('New_Director', ('first_name', 'last_name', 'age', 'position'))


class Director(Human):
    def __init__(self, first_name, last_name, age, position=None):
        super().__init__(first_name, last_name, age, position)
        self.director = None

    def new_human(self, position='Director'):
        return New_Director(self.first_name,
                            self.last_name,
                            self.age,
                            self.position
                            )

    def print_new_human(self):
        print(f'New Director {self.first_name} {self.last_name} was hired.')

    def add_human_list(self):
        self.director = nt('Director', ('first_name', 'last_name'))
        self.__class__.human_list.append(self.director(self.first_name, self.last_name))

    def print_human_list(self):
        print(self.__class__.human_list)


New_Head_Teacher = nt('New_Head_Teacher', ('first_name', 'last_name', 'age', 'position'))


class HeadTeacher(Human):
    def __init__(self, first_name, last_name, age, position=None):
        super().__init__(first_name, last_name, age, position)
        self.head_teacher = None

    def new_human(self, position='HeadTeacher'):
        return New_Head_Teacher(self.first_name,
                                self.last_name,
                                self.age,
                                self.position
                                )

    def print_new_human(self):
        print(f'New HeadTeacher {self.first_name} {self.last_name} was hired.')

    def add_human_list(self):
        self.head_teacher = nt('HeadTeacher', ('first_name', 'last_name'))
        self.__class__.human_list.append(self.head_teacher(self.first_name, self.last_name))

    def print_human_list(self):
        print(self.__class__.human_list)


New_Teacher = nt('New_Teacher', ('first_name', 'last_name', 'age', 'position'))


class Teacher(Human):
    def __init__(self, first_name, last_name, age, position=None):
        super().__init__(first_name, last_name, age, position)
        self.teacher = None

    def new_human(self, position='Teacher'):
        return New_Teacher(self.first_name,
                           self.last_name,
                           self.age,
                           self.position
                           )

    def print_new_human(self):
        print(f'New Teacher {self.first_name} {self.last_name} was hired.')

    def add_human_list(self):
        self.teacher = nt('Teacher', ('first_name', 'last_name'))
        self.__class__.human_list.append(self.teacher(self.first_name, self.last_name))

    def print_human_list(self):
        print(self.__class__.human_list)


New_Student = nt('New_Teacher', ('first_name', 'last_name', 'age', 'position'))


class Student(Human, ABC):
    def __init__(self, first_name, last_name, age, position=None):
        super().__init__(first_name, last_name, age, position)
        self.student = None

    def new_human(self, position='Student'):
        return New_Student(self.first_name,
                           self.last_name,
                           self.age,
                           self.position
                           )

    def print_new_human(self):
        print(f'New Student {self.first_name} {self.last_name} was hired.')

    def add_human_list(self):
        self.student = nt('Student', ('first_name', 'last_name'))
        self.__class__.human_list.append(self.student(self.first_name, self.last_name))

    def print_human_list(self):
        print(self.__class__.human_list)