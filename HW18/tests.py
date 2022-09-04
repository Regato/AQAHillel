import pytest

from School import ClassRoom
from Staff import SexEnum, Student, Teacher


@pytest.fixture(scope="session", autouse=True)
def classroom_scope():
    teacher = Teacher('Test', 'TestTeacher1', 60, SexEnum.WOMEN)
    class_room = ClassRoom('a10', teacher)

    student1 = Student('Test', 'TestStudent1', 16, SexEnum.WOMEN)

    class_room.new_student(student1)

    print('\nTesting is starting...')

    yield class_room

    del class_room
    del teacher
    del student1

    print('\nTesting complete!')
