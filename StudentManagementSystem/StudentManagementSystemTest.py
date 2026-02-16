import unittest

from StudentManagementSystem.Courses import AllCourses
from StudentManagementSystem.MySchool import MySchool
from StudentManagementSystem.Student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mySchool = MySchool()
        self.student = Student("salami AlAmeen", "2065")
        self.course = AllCourses

    def test_that_i_can_get_student_name(self):
        expected ="salami AlAmeen"
        actual = self.student.get_student_name()
        self.assertEqual(expected, actual)

    def test_that_i_can_update_student_name(self):
        self.assertEqual("salami AlAmeen", self.student.get_student_name())
        self.student.update_student_name("Musbau Malik")
        self.assertEqual("Musbau Malik", self.student.get_student_name())

    def test_that_I_can_get_student_id(self):
        expected ="2065"
        actual = self.student.get_student_id()
        self.assertEqual(expected, actual)

    def test_that_i_can_update_id(self):
        self.assertEqual("2065", self.student.get_student_id())
        self.student.update_student_id("1986")
        self.assertEqual("1986", self.student.get_student_id())

    def test_that_when_student_is_created_course_is_empty(self):
        expected = 0
        actual = self.student.get_number_of_courses()
        self.assertEqual(expected, actual)

    def test_that_I_can_add_a_course(self):
        self.assertEqual(0, self.student.get_number_of_courses())
        self.student.add_course("PYT101")
        self.assertEqual(1, self.student.get_number_of_courses())

    def test_that_I_can_add_multiple_courses(self):
        self.assertEqual(0, self.student.get_number_of_courses())
        self.student.add_course("PYT101")
        self.student.add_course("REG101")
        self.student.add_course("SYS101")
        self.assertEqual(3, self.student.get_number_of_courses())

    def test_that_I_can_get_student_grade(self):
        self.assertEqual(0, self.student.get_number_of_courses())
        self.student.add_course("PYT101")
        self.assertEqual(0, self.student.get_grade("PYT101"))

    def test_that_I_can_update_student_grade(self):
        self.assertEqual(0, self.student.get_number_of_courses())
        self.student.add_course("PYT101")
        self.student.add_grade_to_course("PYT101", 60)
        self.assertEqual(60, self.student.get_grade("PYT101"))

    def test_that_initial_number_of_students_is_0(self):
        expected = 0
        actual =  self.student.get_number_of_courses()
        self.assertEqual(actual, expected)

    def test_that_I_can_create_a_student(self):
        self.assertEqual(0, self.mySchool.get_number_of_students())
        self.mySchool.create_student("salami AlAmeen", "2065")
        self.assertEqual(1, self.mySchool.get_number_of_students())

    def test_that_I_can_create_multiple_students(self):
        self.assertEqual(0, self.mySchool.get_number_of_students())
        self.mySchool.create_student("Musbau Bolakale", "2456")
        self.mySchool.create_student("Kolade Luqman", "3436")
        self.mySchool.create_student("Hassan Raheem","53435")
        self.mySchool.create_student("Salau Ayooluwa", "32425")
        self.assertEqual(4, self.mySchool.get_number_of_students())

    def test_that_I_can_get_a_student_name(self):
        self.assertEqual(0, self.mySchool.get_number_of_students())
        self.mySchool.create_student("Musbau Bolakale", "2456")
        self.mySchool.create_student("Kolade Luqman", "3436")
        self.mySchool.create_student("Hassan Raheem", "53435")
        self.mySchool.create_student("Salau Ayooluwa", "32425")
        self.assertEqual("Salau Ayooluwa", self.mySchool.get_student_name("32425"))

    def test_that_I_can_update_a_student_name(self):
        self.assertEqual(0, self.mySchool.get_number_of_students())
        self.mySchool.create_student("Musbau Bolakale", "2456")
        self.mySchool.create_student("Kolade Luqman", "3436")
        self.mySchool.create_student("Hassan Raheem", "53435")
        self.mySchool.create_student("Salau Ayooluwa", "32425")
        self.assertEqual("Salau Ayooluwa", self.mySchool.get_student_name("32425"))
        self.mySchool.update_student_name("32425", "Alimzy")
        self.assertEqual("Alimzy", self.mySchool.get_student_name("32425"))

    def test_that_I_can_get_a_student_courses(self):
        self.assertEqual(0, self.mySchool.get_number_of_students())
        self.mySchool.create_student("Musbau Bolakale", "2456")
        self.mySchool.create_student("Kolade Luqman", "3436")
        self.mySchool.create_student("Hassan Raheem", "53435")
        self.mySchool.create_student("Salau Ayooluwa", "32425")
        self.assertEqual(0, self.mySchool.get_student_courses("32425"))

    def test_that_I_can_add_a_course_to_a_student(self):
        self.assertEqual(0, self.mySchool.get_number_of_students())
        self.mySchool.create_student("Musbau Bolakale", "2456")
        self.mySchool.create_student("Kolade Luqman", "3436")
        self.mySchool.create_student("Hassan Raheem", "53435")
        self.mySchool.create_student("Salau Ayooluwa", "32425")
        self.assertEqual(0, self.mySchool.get_student_courses("32425"))
        self.mySchool.update_student_courses("32425","PHT101")
        self.assertEqual(1, self.mySchool.get_student_courses("32425"))





if __name__ == '__main__':
    unittest.main()
