
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")

students = []



def add_student():
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    
    student = Student(roll_no, name, marks)
    students.append(student)
    print("Student added successfully!\n")

def display_students():
    if len(students) == 0:
        print("No students found!\n")
    else:
        print("\nStudent List:")
        for s in students:
            s.display()
        print()

def search_student():
    roll_no = int(input("Enter Roll No to search: "))
    found = False
    
    for s in students:
        if s.roll_no == roll_no:
            print("Student Found:")
            s.display()
            found = True
            break
    if not found:
        print("Student not found!\n")

def menu():
    while True:
        print("----- Student Management System -----")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")
menu()