class Student:
    def __init__(self, name, roll_no, branch, marks):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.marks = marks

    def display_info(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Branch:", self.branch)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


print("STUDENT RECORD MANAGEMENT SYSTEM")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
marks = float(input("Enter marks: "))

student = Student(name, roll_no, branch, marks)

student.display_info()
student.check_result()
