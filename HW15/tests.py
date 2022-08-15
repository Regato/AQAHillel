import string
import random
from random import randint

from School import ClassRoom
from Staff import Director, HeadTeacher, Teacher, Student
from Staff import SexEnum


# Returns random number in range from first to last
def random_number(first: int, last: int) -> int:
    """Random number function in diapason

        Args:
            first(int): any integer argument
            last(int): any integer argument that > than first argument

        Returns:
            random number
    """
    number_output = randint(first, last)

    return number_output


# Returns random string with lower and UPPER cases
def random_any_string(iteration: int) -> int:
    """Random string of letters function

        Args:
            iteration(int): any integer argument

        Returns:
            random string of letters (upper case +/or lower case)
    """
    letters = string.ascii_letters
    string_output = ''.join(random.choice(letters) for index in range(iteration))

    return string_output


def setup_director():
    random_name = random_any_string(11)
    random_surname = random_any_string(11)
    random_age = random_number(45, 70)
    sex = SexEnum.MEN
    director = Director(random_name, random_surname, random_age, sex)

    return director, random_name, random_surname, random_age, sex


def test_director_name():
    director_result = setup_director()
    assert director_result[0].first_name == director_result[1]


def test_director_surname():
    director_result = setup_director()
    assert director_result[0].last_name == director_result[2]


def test_director_age():
    director_result = setup_director()
    assert director_result[0].age == director_result[3]


def test_director_sex():
    director_result = setup_director()
    assert director_result[0].sex == director_result[4]


def setup_head_teacher():
    random_name = random_any_string(11)
    random_surname = random_any_string(11)
    random_age = random_number(45, 70)
    sex = SexEnum.WOMEN
    head_teacher = HeadTeacher(random_name, random_surname, random_age, sex)

    return head_teacher, random_name, random_surname, random_age, sex


def test_headteacher_name():
    head_teacher_result = setup_head_teacher()
    assert head_teacher_result[0].first_name == head_teacher_result[1]


def test_headteacher_surname():
    head_teacher_result = setup_head_teacher()
    assert head_teacher_result[0].last_name == head_teacher_result[2]


def test_headteacher_age():
    head_teacher_result = setup_head_teacher()
    assert head_teacher_result[0].age == head_teacher_result[3]


def test_headteacher_sex():
    head_teacher_result = setup_head_teacher()
    assert head_teacher_result[0].sex == head_teacher_result[4]


def setup_teacher():
    random_name = random_any_string(11)
    random_surname = random_any_string(11)
    random_age = random_number(45, 70)
    sex = SexEnum.MEN
    teacher = Teacher(random_name, random_surname, random_age, sex)

    return teacher, random_name, random_surname, random_age, sex


def test_teacher_name():
    teacher_result = setup_teacher()
    assert teacher_result[0].first_name == teacher_result[1]


def test_teacher_surname():
    teacher_result = setup_teacher()
    assert teacher_result[0].last_name == teacher_result[2]


def test_teacher_age():
    teacher_result = setup_teacher()
    assert teacher_result[0].age == teacher_result[3]


def test_teacher_sex():
    teacher_result = setup_teacher()
    assert teacher_result[0].sex == teacher_result[4]


def setup_student():
    random_name = random_any_string(11)
    random_surname = random_any_string(11)
    random_age = random_number(45, 70)
    sex = SexEnum.WOMEN
    student = Student(random_name, random_surname, random_age, sex)

    return student, random_name, random_surname, random_age, sex


def test_student_name():
    student_result = setup_student()
    assert student_result[0].first_name == student_result[1]


def test_student_surname():
    student_result = setup_student()
    assert student_result[0].last_name == student_result[2]


def test_student_age():
    student_result = setup_student()
    assert student_result[0].age == student_result[3]


def test_student_sex():
    student_result = setup_student()
    assert student_result[0].sex == student_result[4]


def setup_empty_class():
    teacher = Teacher('Test', 'TestTeacher1', 60, SexEnum.WOMEN)
    class_room = ClassRoom('a10', teacher)

    return class_room


def test_empty_class1():
    class_result = setup_empty_class()
    class_count = len(class_result.__class__.classrooms['a10'])

    assert class_count == 1


def setup_class():
    teacher = Teacher('Test', 'TestTeacher1', 60, SexEnum.WOMEN)
    class_room = ClassRoom('a10', teacher)

    student1 = Student('Test', 'TestStudent1', 16, SexEnum.WOMEN)
    student2 = Student('Test', 'TestStudent2', 15, SexEnum.MEN)
    student3 = Student('Test', 'TestStudent3', 14, SexEnum.WOMEN)
    student4 = Student('Test', 'TestStudent4', 17, SexEnum.MEN)
    student5 = Student('Test', 'TestStudent5', 17, SexEnum.WOMEN)

    class_room.new_student(student1)
    class_room.new_student(student2)
    class_room.new_student(student3)
    class_room.new_student(student4)
    class_room.new_student(student5)

    return class_room


def test_class_count():
    class_result = setup_class()
    class_count = len(class_result.__class__.classrooms['a10'])

    assert class_count == 6


def test_add_student():
    class_result = setup_class()
    student6 = Student('Test', 'TestStudent6', 15, SexEnum.MEN)
    class_result.new_student(student6)
    class_count = len(class_result.__class__.classrooms['a10'])

    assert class_count == 7


def test_remove_student():
    student6 = Student('Test', 'TestStudent6', 15, SexEnum.MEN)
    class_result = setup_class()
    class_result.new_student(student6)
    class_count1 = len(class_result.__class__.classrooms['a10'])

    assert class_count1 == 7

    class_result.delete_student(student6)
    class_count2 = len(class_result.__class__.classrooms['a10'])

    assert class_count2 == 6