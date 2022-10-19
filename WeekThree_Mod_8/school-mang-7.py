class Student:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id

class Course:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher

class Teacher:
    def __init__(self,name,course):
        self.name = name
        self.course = course

class School:
    def __init__(self,name,teachers,students,courses):
        self.name = name
        self.teachers = teachers
        self.students = students
        self.courses = courses

    def get_student(self):
        for student in self.students:
            print(student.name)


school_name = "University of Phitron"
ds_course = Course("Data Structure","Einstein")
teacher_1 = Teacher("Einstein",ds_course)
algo_course = Course("Algorithm","Edison")
teacher_2 = Teacher("Edison",algo_course)

student_1 = Student("Rohmot",17,76)
student_2 = Student("Keramot",16,77)
student_3 = Student("Alia Bhatt",17,78)

teachers = [teacher_1,teacher_2]
students = [student_1,student_2,student_3]
courses = [ds_course,algo_course]

my_school = School(school_name,teachers,students,courses)

my_school.get_student()