class PyATB:
    student_address = None
    student_name = None
    student_email = None
    student_course = None
    student_attendance = None
    attendance_grade = None

    def __init__(self, student_address, name, email, course, attendance):
        self.student_address = student_address
        self.student_name = name
        self.student_email = email
        self.student_course = course
        self.student_attendance = attendance

    def student_information(self):
        return (f"Hello {self.student_name} with {self.student_email} of {self.student_address} "
                f"enrolled in {self.student_course} with {self.student_attendance} ")

    def student_attendance_grade(self):
        if self.student_attendance < 50:
            self.attendance_grade = "F"
        elif 50 <= self.student_attendance <= 60:
            self.attendance_grade = "E"
        elif 61 <= self.student_attendance <= 70:
            self.attendance_grade = "D"
        elif 71 <= self.student_attendance <= 80:
            self.attendance_grade = "C"
        elif 81 <= self.student_attendance <= 90:
            self.attendance_grade = "B"
        elif 91 <= self.student_attendance <= 100:
            self.attendance_grade = "A"
        else:
            self.attendance_grade = "Not Applicable"

        return self.attendance_grade

    def student_print_course(self):
        return self.student_course


obj1 = PyATB("red@gmail.com", "Red", "plot no 145", "python", 56)
print(obj1.student_print_course())
print(obj1.student_information())
print(obj1.student_attendance_grade())

email = input("Enter email of student")
address = input("Enter address of student")
name = input("Enter name of student")
course = input("Enter course of student")
attendance = int(input("Enter the attendance in numbers between 0 to 100"))

obj2 = PyATB(address, name, email, course, attendance)
print(obj2.student_print_course())
print(obj2.student_information())
print(obj2.student_attendance_grade())

