from StudentManagementSystem.Courses import AllCourses

class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        # self.grade = 0
        self.courses = {}


    def get_student_name(self):
        return self.name

    def  update_student_name(self,name ):
        self.name = name

    def get_student_id(self):
        return self.id

    def update_student_id(self,id):
        self.id = id

    def add_course(self, course_code):

        for course in AllCourses:
            if course_code == course.name:
                if course_code in self.courses:
                    raise ValueError("Course already exists")
                self.courses[course.name] = {"title":course.value,"grade":0}

    def get_number_of_courses(self):
        return len(self.courses)

    def add_grade_to_course(self,course_code,grade):
        if course_code not in self.courses:
            raise ValueError("Course does not exists")
        self.courses[course_code]["grade"] = grade


    def get_grade(self,course_code):
        for course in AllCourses:
            if course_code == course.name:
                return self.courses[course.name]["grade"]
            raise ValueError("Course does not exists")

