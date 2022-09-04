import pytest

from tests import classroom_scope
from Staff import SexEnum, Student


@pytest.fixture(scope="module")
def student_scope():
    student = Student('Test', 'TestStudent3', 15, SexEnum.MEN)

    print('\nTesting is starting...')

    yield student

    del student

    print('\nTesting complete!')


@pytest.mark.usefixtures('student_scope')
@pytest.mark.usefixtures('classroom_scope')
def test_add_student(classroom_scope, student_scope):
    class_count_before = len(classroom_scope.__class__.classrooms['a10'])
    classroom_scope.new_student(student_scope)
    class_count_after = len(classroom_scope.__class__.classrooms['a10'])

    assert class_count_before == 2
    assert class_count_after == 3


@pytest.mark.usefixtures('student_scope')
@pytest.mark.usefixtures('classroom_scope')
def test_remove_student(classroom_scope, student_scope):
    class_count_before2 = len(classroom_scope.__class__.classrooms['a10'])
    classroom_scope.delete_student(student_scope)
    class_count_after2 = len(classroom_scope.__class__.classrooms['a10'])

    assert class_count_before2 == 3
    assert class_count_after2 == 2