from abc import ABC
from abc import abstractmethod
from collections import namedtuple as nt


# Named tuple for Rewards class
Finance_Fond = nt('Finance_Fond', ('integer', 'last_name'))
Student_Required = nt('Student_Required', ('integer', 'last_name'))


class Rewards(ABC):
    """Takes human_object (class object)"""
    finance_fond = list()
    student_required = list()

    def __init__(self, human_object):
        self.human_object = human_object
        # Executing class method fond_accounting
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
    """Takes human_object (class object)"""
    grades = list()

    def __init__(self, human_object):
        super().__init__(human_object)
        # Student paying for school when he was added to school
        self.__class__.pay_for_school(self)

    def fond_accounting(self):
        # School fond -1 student needed
        self.__class__.student_required.append(Student_Required(-1, self.human_object.last_name))

    def print_fond_required(self):
        # Get all student needed list for school fond
        finance_list = [index.integer for index in self.__class__.student_required]
        sum_finance = sum(finance_list)

        # Check is school fond needs students, if yes how much
        if sum_finance < 0:
            print('School is full of students!')
        else:
            print(f'School fond need {sum_finance} students!')

    def pay_for_school(self):
        # Student paying for school
        self.__class__.finance_fond.append(Finance_Fond(10000, self.human_object.last_name))
        print('Student paid 10000 to financial fond of school.')

    def personal_reward(self):
        # Student got grade
        grade_values = [value.grade for value in self.__class__.grades]
        average_grade = sum(grade_values)

        print(f'Average grade for student {self.human_object.last_name} is {average_grade}')

    def get_all_rewards(self):
        # Get all grades for all students
        return self.__class__.grades

    def report_reward(self, grade):
        # Report new grade for student
        self.grades.append(New_Grade(self.human_object.first_name,
                                     self.human_object.last_name,
                                     grade
                                     )
                           )
        print(f'Student got grade {grade}! Greetings for this student.')

    def print_financial_fond(self):
        # Print how much money has school fond
        finance_list = [finance.integer for finance in self.__class__.finance_fond]
        sum_finance = sum(finance_list)
        print(f'Finance fond of school is {sum_finance}.')


class SalaryDirector(Rewards):
    """Takes human_object (class object)"""
    def __init__(self, human_object):
        super().__init__(human_object)
        self.director_fond = 0
        # Pay salary to director when director was added to school
        self.__class__.personal_reward(self)

    def fond_accounting(self):
        # School needs 2 student because director salary is 20000 and student payment is 10000
        self.__class__.student_required.append(Student_Required(2, self.human_object.last_name))

    def print_fond_required(self):
        # Get all student needed list for school fond
        finance_list = [index.integer for index in self.__class__.student_required]
        sum_finance = sum(finance_list)

        # Check is school fond needs students, if yes how much
        if sum_finance < 0:
            print('School is full of students!')
        else:
            print(f'School fond need {sum_finance} students!')

    def personal_reward(self):
        # Pay salary to Director
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
        # Print how much money has Director
        print(f'Director finances are {self.director_fond}')

    def report_reward(self, value=20000):
        print(f'Director {self.human_object.first_name} '
              f'has self fond {self.director_fond} with {value} salary')

    def print_financial_fond(self):
        # Print how much money has school fond
        finance_list = [finance.integer for finance in self.__class__.finance_fond]
        sum_finance = sum(finance_list)
        print(f'Finance fond of school is {sum_finance}.')


class SalaryHeadTeacher(Rewards):
    """Takes human_object (class object)"""
    def __init__(self, human_object):
        super().__init__(human_object)
        self.head_teacher_fond = 0
        # Pay salary to director when HeadTeacher was added to school
        self.__class__.personal_reward(self)

    def fond_accounting(self):
        # School needs 2 student because HeadTeacher salary is 15000 and student payment is 10000
        self.__class__.student_required.append(Student_Required(2, self.human_object.last_name))

    def print_fond_required(self):
        # Get all student needed list for school fond
        finance_list = [index.integer for index in self.__class__.student_required]
        sum_finance = sum(finance_list)

        # Check is school fond needs students, if yes how much
        if sum_finance < 0:
            print('School is full of students!')
        else:
            print(f'School fond need {sum_finance} students!')

    def personal_reward(self):
        # Pay salary to HeadTeacher
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
        # Print how much money has HeadTeacher
        print(f'HeadTeacher finances are {self.head_teacher_fond}')

    def report_reward(self, value=6000):
        print(f'HeadTeacher {self.human_object.first_name} '
              f'has self fond {self.head_teacher_fond} with {value} salary')

    def print_financial_fond(self):
        # Print how much money has school fond
        finance_list = [finance.integer for finance in self.__class__.finance_fond]
        sum_finance = sum(finance_list)
        print(f'Finance fond of school is {sum_finance}.')


class SalaryTeacher(Rewards):
    """Takes human_object (class object)"""
    def __init__(self, human_object):
        super().__init__(human_object)
        self.teacher_fond = 0
        # Pay salary to Teacher when director was added to school
        self.__class__.personal_reward(self)

    def fond_accounting(self):
        # School needs 2 student because HeadTeacher salary is 15000 and student payment is 10000
        self.__class__.student_required.append(Student_Required(1, self.human_object.last_name))

    def print_fond_required(self):
        # Get all student needed list for school fond
        finance_list = [index.integer for index in self.__class__.student_required]
        sum_finance = sum(finance_list)

        # Check is school fond needs students, if yes how much
        if sum_finance < 0:
            print('School is full of students!')
        else:
            print(f'School fond need {sum_finance} students!')

    def personal_reward(self):
        # Pay salary to Teacher
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
        # Print how much money has Teacher
        print(f'Teacher finances are {self.teacher_fond}')

    def report_reward(self, value=6000):
        print(f'Teacher {self.human_object.first_name} '
              f'has self fond {self.teacher_fond} with {value} salary')

    def print_financial_fond(self):
        # Print how much money has school fond
        finance_list = [finance.integer for finance in self.__class__.finance_fond]
        sum_finance = sum(finance_list)
        print(f'Finance fond of school is {sum_finance}.')
