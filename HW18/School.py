from abc import ABC
from abc import abstractmethod
from collections import namedtuple as nt


class EduInstitution(ABC):
    """Takes name and graduation attributes"""
    inst_list = list()

    def __init__(self, name, graduation):
        self.name = name
        self.graduation = graduation

    @abstractmethod
    def new_institution(self):
        pass


New_School = nt('New_School', ('name', 'graduation'))


class School(EduInstitution):
    """Got the same takes as parent class EduInstitution"""
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
    """Takes parent class arguments and classroom_name, teacher_object (class object)"""

    def __init__(self, classroom_name, teacher_object, name=None, graduation=None):
        super().__init__(name, graduation)
        self.classroom_name = classroom_name
        self.teacher_object = teacher_object
        self.__class__.new_classroom(self)

    def new_classroom(self):
        # Add new classroom with classroom teacher
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
        # Add student to class
        add_student = (New_Classroom(self.classroom_name,
                                     student_object.position,
                                     student_object.first_name,
                                     student_object.last_name
                                     )
                       )

        for student in self.__class__.classrooms[self.classroom_name]:
            if add_student in self.__class__.classrooms[self.classroom_name]:
                print('Cannot add this student to the classroom because he is already added.')
            else:
                self.__class__.classrooms[self.classroom_name].append(add_student)
                print(f'New student {student_object.first_name} '
                      f'{student_object.last_name} was added to {self.classroom_name}'
                      )
                break

    def print_classroom_list(self):
        # Classroom list
        print(f'Classroom list is: {self.__class__.classrooms[self.classroom_name]}')

    def delete_student(self, student_object):
        # Delete student from class
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
        try:
            del self.__class__.classrooms[self.classroom_name]
        except KeyError:
            pass
        pass
