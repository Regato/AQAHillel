from Rewards import SalaryDirector, SalaryHeadTeacher, SalaryTeacher, Grades
from Staff import Director, HeadTeacher, Teacher, Student
from Staff import SexEnum
from School import School, ClassRoom

if __name__ == '__main__':
    school = School('Hillel IT School', 'High')

    director = Director('Test', 'TestDirector', 65, sex=SexEnum.MEN)
    headteacher = HeadTeacher('Test', 'TestHeadteacher', 63, SexEnum.WOMEN)
    teacher1 = Teacher('Test', 'TestTeacher1', 60, SexEnum.WOMEN)
    teacher2 = Teacher('Test', 'TestTeacher2', 45, SexEnum.WOMEN)
    teacher3 = Teacher('Test', 'TestTeacher3', 35, SexEnum.WOMEN)

    director.print_sex()  # Men
    headteacher.print_sex()  # Women
    director.print_human_list()  # People list with sex attribute for every human

    salary_director = SalaryDirector(director)
    salary_head_teacher = SalaryHeadTeacher(headteacher)
    salary_teacher1 = SalaryTeacher(teacher1)
    salary_teacher2 = SalaryTeacher(teacher2)
    salary_teacher3 = SalaryTeacher(teacher3)

    salary_teacher3.print_fond_required()
    director.print_human_list()

    student1 = Student('Test', 'TestStudent1', 16, SexEnum.WOMEN)
    student2 = Student('Test', 'TestStudent2', 15, SexEnum.MEN)
    student3 = Student('Test', 'TestStudent3', 14, SexEnum.WOMEN)
    student4 = Student('Test', 'TestStudent4', 17, SexEnum.MEN)
    student5 = Student('Test', 'TestStudent5', 17, SexEnum.WOMEN)
    student6 = Student('Test', 'TestStudent6', 15, SexEnum.MEN)
    student7 = Student('Test', 'TestStudent7', 14, SexEnum.WOMEN)
    student8 = Student('Test', 'TestStudent8', 16, SexEnum.MEN)
    student9 = Student('Test', 'TestStudent9', 14, SexEnum.WOMEN)
    student10 = Student('Test', 'TestStudent10', 15, SexEnum.MEN)

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







