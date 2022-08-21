from abc import ABC
from abc import abstractmethod
from collections import namedtuple as nt


class EduInstitution(ABC):
    inst_list = list()

    def __init__(self, name, graduation):
        self.name = name
        self.graduation = graduation

    @abstractmethod
    def new_institution(self):
        pass


New_School = nt('New_School', ('name', 'graduation'))


class School(EduInstitution):
    classrooms = dict()

    def new_institution(self):
        return New_School(self.name, self.graduation)

    def new_classroom(self):
        pass

    def new_student(self, student_object):
        pass

    def print_classroom_list(self):
        pass

    def delete_student(self, student_object):
        pass


New_Classroom = nt('Classroom', ('name', 'position', 'first_name', 'last_name'))


class ClassRoom(School):

    def __init__(self, classroom_name, teacher_object, name=None, graduation=None):
        super().__init__(name, graduation)
        self.classroom_name = classroom_name
        self.teacher_object = teacher_object
        self.__class__.new_classroom(self)

    def new_classroom(self):
        classroom = (New_Classroom(self.classroom_name,
                                   self.teacher_object.position,
                                   self.teacher_object.first_name,
                                   self.teacher_object.last_name
                                   )
                     )
        self.__class__.classrooms[str(self.classroom_name)] = [classroom]
        print(f'New classroom {self.classroom_name} was created with teacher '
              f'{self.teacher_object.first_name} {self.teacher_object.last_name}'
              )

    def new_student(self, student_object):
        student = (New_Classroom(self.classroom_name,
                                 student_object.position,
                                 student_object.first_name,
                                 student_object.last_name
                                 )
                   )
        self.__class__.classrooms[self.classroom_name].append(student)
        print(f'New student {student_object.first_name} '
              f'{student_object.last_name} was added to {self.classroom_name}'
              )

    def print_classroom_list(self):
        print(f'Classroom list is: {self.__class__.classrooms[self.classroom_name]}')

    def delete_student(self, student_object):
        student = (New_Classroom(self.classroom_name,
                                 student_object.position,
                                 student_object.first_name,
                                 student_object.last_name
                                 )
                   )
        self.__class__.classrooms[self.classroom_name].remove(student)
        print(f'Student {student_object.first_name} {student_object.last_name}'
              f' was removed from {self.classroom_name}'
              )

    def print_all(self):
        print(f'All classes list: {self.__class__.classrooms}')

    def __del__(self):
        del self.__class__.classrooms[self.classroom_name]
        pass
