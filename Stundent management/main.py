
class Student:
    def __init__(self, usn, name, marks):
        self.usn = usn
        self.name = name
        self.marks = marks

    def display(self):
        print("USN:", self.usn)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("=======================================")


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        usn = input("Enter USN: ")

        for student in self.students:
            if student.usn == usn:
                print("Student with this USN already exists!")
                return

        name = input("Enter the name: ")
        marks = float(input("Enter the marks: "))

        student = Student(usn, name, marks)
        self.students.append(student)

        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No students found!")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        usn = input("Enter USN to search: ")

        for student in self.students:
            if student.usn == usn:
                student.display()
                return

        print("Student not found!")

    def delete_student(self):
        usn = input("Enter USN to delete: ")

        for student in self.students:
            if student.usn == usn:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found!")


# Main program
sm = StudentManagement()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sm.add_student()

    elif choice == "2":
        sm.display_students()

    elif choice == "3":
        sm.search_student()

    elif choice == "4":
        sm.delete_student()

    elif choice == "5":
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice! Try again.")



