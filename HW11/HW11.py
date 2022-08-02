from abc import ABC
from abc import abstractmethod
from collections import namedtuple as nt


New_School = nt('New_School', ('name', 'graduation'))


class EduInstitution(ABC):
    inst_list = list()

    def __init__(self, name, graduation):
        self.name = name
        self.graduation = graduation

    @abstractmethod
    def new_institution(self):
        pass


class School(EduInstitution):
    classrooms = dict()

    def new_institution(self):
        return New_School(self.name, self.graduation)

    def new_classroom(self):
        pass

    def new_student(self, student):
        pass

    def print_classroom_list(self):
        pass

    def delete_student(self, student):
        pass


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


Finance_Fond = nt('Finance_Fond', ('integer', 'last_name'))
Student_Required = nt('Student_Required', ('integer', 'last_name'))


class Rewards(ABC):
    finance_fond = list()
    student_required = list()

    def __init__(self, human_object):
        self.human_object = human_object
        self.__class__.fond_accounting(self)

    @abstractmethod
    def fond_accounting(self):
        pass

    @abstractmethod
    def print_fond_required(self):
        pass

    @abstractmethod
    def personal_reward(self):
        pass

    @abstractmethod
    def get_all_rewards(self):
        pass

    @abstractmethod
    def report_reward(self, reward):
        pass

    @abstractmethod
    def print_financial_fond(self):
        pass


New_Grade = nt('New_Grade', ('first_name', 'last_name', 'grade'))


class Grades(Rewards):
    grades = list()

    def __init__(self, human_object):
        super().__init__(human_object)
        self.__class__.pay_for_school(self)

    def fond_accounting(self):
        self.__class__.student_required.append(Student_Required(-1, self.human_object.last_name))

    def print_fond_required(self):
        finance_list = [index.integer for index in self.__class__.student_required]
        sum_finance = sum(finance_list)

        if sum_finance < 0:
            print('School is full of students!')
        else:
            print(f'School fond need {sum_finance} students!')

    def pay_for_school(self):
        self.__class__.finance_fond.append(Finance_Fond(10000, self.human_object.last_name))
        print('Student paid 10000 to financial fond of school.')

    def personal_reward(self):
        grade_values = [value.grade for value in self.__class__.grades]
        average_grade = sum(grade_values)

        print(f'Average grade for student {self.human_object.last_name} is {average_grade}')

    def get_all_rewards(self):
        return self.__class__.grades

    def report_reward(self, grade):
        self.grades.append(New_Grade(self.human_object.first_name,
                                     self.human_object.last_name,
                                     grade
                                     )
                           )
        print(f'Student got grade {grade}! Greetings for this student.')

    def print_financial_fond(self):
        finance_list = [finance.integer for finance in self.__class__.finance_fond]
        sum_finance = sum(finance_list)
        print(f'Finance fond of school is {sum_finance}.')


class SalaryDirector(Rewards):
    def __init__(self, human_object):
        super().__init__(human_object)
        self.director_fond = 0
        self.__class__.personal_reward(self)

    def fond_accounting(self):
        self.__class__.student_required.append(Student_Required(2, self.human_object.last_name))

    def print_fond_required(self):
        finance_list = [index.integer for index in self.__class__.student_required]
        sum_finance = sum(finance_list)

        if sum_finance < 0:
            print('School is full of students!')
        else:
            print(f'School fond need {sum_finance} students!')

    def personal_reward(self):
        finance_list = [finance.integer for finance in self.__class__.finance_fond]
        sum_finance = sum(finance_list)

        if sum_finance >= 20000:
            self.__class__.finance_fond.append(Finance_Fond(-20000, self.human_object.last_name))
            self.director_fond += 20000
            print(f'Salary 20000 was paid for Teacher '
                  f'{self.human_object.first_name} '
                  f'{self.human_object.last_name}'
                  )
        else:
            print(f'Not enough money in School fond! It has {self.__class__.finance_fond}')

    def get_all_rewards(self):
        print(f'Director finances are {self.director_fond}')

    def report_reward(self, value=20000):
        print(f'Director {self.human_object.first_name} '
              f'has self fond {self.director_fond} with {value} salary')

    def print_financial_fond(self):
        finance_list = [finance.integer for finance in self.__class__.finance_fond]
        sum_finance = sum(finance_list)
        print(f'Finance fond of school is {sum_finance}.')


class SalaryHeadTeacher(Rewards):
    def __init__(self, human_object):
        super().__init__(human_object)
        self.head_teacher_fond = 0
        self.__class__.personal_reward(self)

    def fond_accounting(self):
        self.__class__.student_required.append(Student_Required(2, self.human_object.last_name))

    def print_fond_required(self):
        finance_list = [index.integer for index in self.__class__.student_required]
        sum_finance = sum(finance_list)

        if sum_finance < 0:
            print('School is full of students!')
        else:
            print(f'School fond need {sum_finance} students!')

    def personal_reward(self):
        finance_list = [finance.integer for finance in self.__class__.finance_fond]
        sum_finance = sum(finance_list)

        if sum_finance >= 15000:
            self.__class__.finance_fond.append(Finance_Fond(-15000, self.human_object.last_name))
            self.head_teacher_fond += 15000
            print(f'Salary 15000 was paid for Teacher '
                  f'{self.human_object.first_name} '
                  f'{self.human_object.last_name}'
                  )
        else:
            print(f'Not enough money in School fond! It has {self.__class__.finance_fond}')

    def get_all_rewards(self):
        print(f'HeadTeacher finances are {self.head_teacher_fond}')

    def report_reward(self, value=6000):
        print(f'HeadTeacher {self.human_object.first_name} '
              f'has self fond {self.head_teacher_fond} with {value} salary')

    def print_financial_fond(self):
        finance_list = [finance.integer for finance in self.__class__.finance_fond]
        sum_finance = sum(finance_list)
        print(f'Finance fond of school is {sum_finance}.')


class SalaryTeacher(Rewards):
    def __init__(self, human_object):
        super().__init__(human_object)
        self.teacher_fond = 0
        self.__class__.personal_reward(self)

    def fond_accounting(self):
        self.__class__.student_required.append(Student_Required(1, self.human_object.last_name))

    def print_fond_required(self):
        finance_list = [index.integer for index in self.__class__.student_required]
        sum_finance = sum(finance_list)

        if sum_finance < 0:
            print('School is full of students!')
        else:
            print(f'School fond need {sum_finance} students!')

    def personal_reward(self):
        finance_list = [finance.integer for finance in self.__class__.finance_fond]
        sum_finance = sum(finance_list)

        if sum_finance >= 6000:
            self.__class__.finance_fond.append(Finance_Fond(-6000, self.human_object.last_name))
            self.teacher_fond += 6000
            print(f'Salary 6000 was paid for Teacher '
                  f'{self.human_object.first_name} '
                  f'{self.human_object.last_name}'
                  )
        else:
            print(f'Not enough money in School fond! It has {self.__class__.finance_fond}')

    def get_all_rewards(self):
        print(f'Teacher finances are {self.teacher_fond}')

    def report_reward(self, value=6000):
        print(f'Teacher {self.human_object.first_name} '
              f'has self fond {self.teacher_fond} with {value} salary')

    def print_financial_fond(self):
        finance_list = [finance.integer for finance in self.__class__.finance_fond]
        sum_finance = sum(finance_list)
        print(f'Finance fond of school is {sum_finance}.')


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


if __name__ == '__main__':
    school = School('Hillel IT School', 'High')

    director = Director('Test', 'Director', 65)
    headteacher = HeadTeacher('Test', 'Headteacher', 63)
    teacher1 = Teacher('Test', 'Teacher1', 60)
    teacher2 = Teacher('Test', 'Teacher2', 45)
    teacher3 = Teacher('Test', 'Teacher3', 35)

    salary_director = SalaryDirector(director)
    salary_head_teacher = SalaryHeadTeacher(headteacher)
    salary_teacher1 = SalaryTeacher(teacher1)
    salary_teacher2 = SalaryTeacher(teacher2)
    salary_teacher3 = SalaryTeacher(teacher3)

    salary_teacher3.print_fond_required()
    director.print_human_list()

    student1 = Student('Test', 'Student1', 16)
    student2 = Student('Test', 'Student2', 15)
    student3 = Student('Test', 'Student3', 14)
    student4 = Student('Test', 'Student4', 17)
    student5 = Student('Test', 'Student5', 17)
    student6 = Student('Test', 'Student6', 15)
    student7 = Student('Test', 'Student7', 14)
    student8 = Student('Test', 'Student8', 16)
    student9 = Student('Test', 'Student9', 14)
    student10 = Student('Test', 'Student10', 15)

    grade_student1 = Grades(student1)
    grade_student2 = Grades(student2)
    grade_student3 = Grades(student3)
    grade_student4 = Grades(student4)
    grade_student5 = Grades(student5)
    grade_student6 = Grades(student6)
    grade_student7 = Grades(student7)
    grade_student8 = Grades(student8)
    grade_student9 = Grades(student9)
    grade_student10 = Grades(student10)

    grade_student10.report_reward(10)
    grade_student10.report_reward(12)
    grade_student10.report_reward(9)
    print(grade_student10.get_all_rewards())
    grade_student10.personal_reward()

    director.print_human_list()
    salary_director.print_financial_fond()
    salary_director.print_fond_required()

    class_b10 = ClassRoom('b10', teacher1)
    class_a10 = ClassRoom('a10', teacher2)

    class_b10.print_classroom_list()
    class_a10.print_classroom_list()

    class_b10.new_student(student1)
    class_b10.new_student(student2)
    class_b10.new_student(student3)
    class_b10.new_student(student4)
    class_b10.new_student(student5)

    class_a10.new_student(student6)
    class_a10.new_student(student7)
    class_a10.new_student(student8)
    class_a10.new_student(student9)
    class_a10.new_student(student10)

    class_b10.print_classroom_list()
    class_a10.print_classroom_list()

    class_b10.delete_student(student5)
    class_b10.print_classroom_list()

    class_a10.print_all()
    del class_b10
    class_a10.print_all()







