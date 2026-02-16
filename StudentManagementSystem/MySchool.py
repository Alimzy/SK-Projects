from StudentManagementSystem.Courses import AllCourses
from StudentManagementSystem.Student import Student

class MySchool:
    def __init__(self):
        self.my_students = {}

    def create_student(self, name, id):
        student = Student(name, id)
        self.my_students[id] = student

    def get_number_of_students(self):
        return len(self.my_students)

    def get_student_name(self, id):
        return self.my_students[id].name

    def update_student_name(self, id,new_name):
        self.my_students[id].name = new_name

    def get_student_courses(self, id):
        return len(self.my_students[id].courses)

    def update_student_courses(self, id, course_code):
        for course in AllCourses:
            if course_code == course.name:
                if course_code in self.my_students[id].courses:
                    raise ValueError("Course already exists")
            self.my_students[id].courses[course_code] = {"title":course.value,"grade":0}

