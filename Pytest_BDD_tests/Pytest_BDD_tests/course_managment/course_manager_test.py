from pytest_bdd import scenario, given, when, then
from course_manager import CourseManager

# Fixture to instantiate the course manager
@scenario('course_manager.feature', 'Create a new course')
def test_create_course():
    pass

@scenario('course_manager.feature', 'Enroll a student in a course')
def test_enroll_student():
    pass

@scenario('course_manager.feature', 'Enroll multiple students in a course')
def test_enroll_multiple_students():
    pass

@scenario('course_manager.feature', 'Enroll a student in a non-existent course')
def test_enroll_nonexistent_course():
    pass

# Step definitions
@given('a course manager')
def course_manager():
    return CourseManager()

@when('I create a course named "<course_name>"')
def step_create_course(course_manager, course_name):
    course_manager.create_course(course_name)

@given('a course named "<course_name>"')
def step_given_course(course_manager, course_name):
    course_manager.create_course(course_name)

@when('I enroll the student "<student_name>" in the course "<course_name>"')
def step_enroll_student(course_manager, student_name, course_name):
    try:
        course_manager.enroll_student(student_name, course_name)
    except ValueError as e:
        course_manager.error_message = str(e)

@when('I enroll the students "<student_list>" in the course "<course_name>"')
def step_enroll_multiple_students(course_manager, student_list, course_name):
    students = [student.strip() for student in student_list.split(',')]
    for student in students:
        course_manager.enroll_student(student, course_name)

@then('the course "<course_name>" should exist')
def step_course_exists(course_manager, course_name):
    assert course_name in course_manager.courses

@then('"<student_name>" should be enrolled in the course "<course_name>"')
def step_student_enrolled(course_manager, student_name, course_name):
    assert course_manager.get_course_for_student(student_name) == course_name

@then('"<course_name>" should have "<student_list>" as students')
def step_course_has_students(course_manager, course_name, student_list):
    students = [student.strip() for student in student_list.split(',')]
    assert set(course_manager.get_students_in_course(course_name)) == set(students)

@then('an error should be raised')
def step_raise_error(course_manager):
    assert hasattr(course_manager, 'error_message') and course_manager.error_message is not None
