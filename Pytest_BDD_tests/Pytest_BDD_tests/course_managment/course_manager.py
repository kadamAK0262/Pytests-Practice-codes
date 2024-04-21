class CourseManager:
    def __init__(self):
        self.courses = {}
        self.students = {}

    def create_course(self, course_name):
        self.courses[course_name] = []

    def enroll_student(self, student_name, course_name):
        if course_name in self.courses:
            self.students[student_name] = course_name
            self.courses[course_name].append(student_name)
        else:
            raise ValueError(f"Course '{course_name}' does not exist.")

    def get_students_in_course(self, course_name):
        return self.courses.get(course_name, [])

    def get_course_for_student(self, student_name):
        return self.students.get(student_name, None)
