import pytest

from tests import classroom_scope
from Staff import Student
from Staff import SexEnum


@pytest.fixture(scope="function", autouse=True)
def student_scope():
    student = Student('Test', 'TestStudent2', 15, SexEnum.MEN)

    print('\nTesting is starting...')

    yield student

    del student

    print('\nTesting complete!')


@pytest.mark.usefixtures('student_scope')
@pytest.mark.usefixtures('classroom_scope')
def test_remove_student(classroom_scope, student_scope):
    class_count_before1 = len(classroom_scope.__class__.classrooms['a10'])
    classroom_scope.new_student(student_scope)
    class_count_after1 = len(classroom_scope.__class__.classrooms['a10'])

    assert class_count_before1 < class_count_after1

    class_count_before2 = len(classroom_scope.__class__.classrooms['a10'])
    classroom_scope.delete_student(student_scope)
    class_count_after2 = len(classroom_scope.__class__.classrooms['a10'])

    assert class_count_before2 > class_count_after2
