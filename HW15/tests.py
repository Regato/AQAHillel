import pytest

from School import ClassRoom
from Staff import Director, HeadTeacher, Teacher, Student
from Staff import SexEnum


@pytest.fixture(scope="session")
def director():
    director = Director('Test', 'Director', 60, SexEnum.MEN)

    return director


def test_director_name(director):
    assert director.first_name == 'Test'


def test_director_surname(director):
    assert director.last_name == 'Director'


def test_director_age(director):
    assert director.age == 60


def test_director_sex(director):
    assert director.sex == SexEnum.MEN


@pytest.fixture(scope="session")
def head_teacher():
    head_teacher = HeadTeacher('Test', 'HeadTeacher', 45, SexEnum.WOMEN)

    return head_teacher


def test_headteacher_name(head_teacher):
    assert head_teacher.first_name == 'Test'


def test_headteacher_surname(head_teacher):
    assert head_teacher.last_name == 'HeadTeacher'


def test_headteacher_age(head_teacher):
    assert head_teacher.age == 45


def test_headteacher_sex(head_teacher):
    assert head_teacher.sex == SexEnum.WOMEN


@pytest.fixture(scope="session")
def teacher():
    teacher = Teacher('Test', 'Teacher', 35, SexEnum.MEN)

    return teacher


def test_teacher_name(teacher):
    assert teacher.first_name == 'Test'


def test_teacher_surname(teacher):
    assert teacher.last_name == 'Teacher'


def test_teacher_age(teacher):
    assert teacher.age == 35


def test_teacher_sex(teacher):
    assert teacher.sex == SexEnum.MEN


@pytest.fixture(scope="session")
def student():
    student = Student('Test', 'Student', 16, SexEnum.WOMEN)

    return student


def test_student_name(student):
    assert student.first_name == 'Test'


def test_student_surname(student):
    assert student.last_name == 'Student'


def test_student_age(student):
    assert student.age == 16


def test_student_sex(student):
    assert student.sex == SexEnum.WOMEN


@pytest.fixture(scope="session")
def empty_class():
    teacher = Teacher('Test', 'TestTeacher1', 60, SexEnum.WOMEN)
    class_room = ClassRoom('a10', teacher)

    return class_room


def test_empty_class1(empty_class):
    class_count = len(empty_class.__class__.classrooms['a10'])

    assert class_count == 1


@pytest.fixture(scope="session")
def full_class():
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


def test_class_count(full_class):
    class_count = len(full_class.__class__.classrooms['a10'])

    assert class_count == 6


def test_add_student(full_class):
    student6 = Student('Test', 'TestStudent6', 15, SexEnum.MEN)
    full_class.new_student(student6)
    class_count = len(full_class.__class__.classrooms['a10'])

    assert class_count == 7


def test_remove_student(full_class):
    student6 = Student('Test', 'TestStudent6', 15, SexEnum.MEN)
    full_class.new_student(student6)
    class_count1 = len(full_class.__class__.classrooms['a10'])

    assert class_count1 == 8

    full_class.delete_student(student6)
    class_count2 = len(full_class.__class__.classrooms['a10'])

    assert class_count2 == 7