import pytest
from course_manager import CourseManager

@pytest.fixture
def course_manager():
    return CourseManager()

def test_create_course(course_manager):
    course_manager.create_course("History")
    assert "History" in course_manager.courses

def test_enroll_student(course_manager):
    course_manager.create_course("Math")
    course_manager.enroll_student("John", "Math")
    assert course_manager.get_course_for_student("John") == "Math"

def test_enroll_multiple_students(course_manager):
    course_manager.create_course("Biology")
    students = ["Alice", "Bob", "Charlie"]
    for student in students:
        course_manager.enroll_student(student, "Biology")

    assert set(course_manager.get_students_in_course("Biology")) == set(students)

def test_enroll_nonexistent_course(course_manager):
    with pytest.raises(ValueError, match="Course 'Physics' does not exist."):
        course_manager.enroll_student("Dave", "Physics")

