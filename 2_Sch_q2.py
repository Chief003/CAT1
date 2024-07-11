class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}  # Dictionary to hold subjects and grades

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        total = sum(self.grades.values())
        count = len(self.grades)
        return total / count

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students in the classroom.")
        else:
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student.get_average_grade()
        return None

    def get_class_average(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            return None
        return total / count

# Demonstration of functionalities

# Create Classroom instance
classroom = Classroom()

# Create Student instances
student1 = Student("Alice")
student2 = Student("Bob")

# Add grades to students
student1.add_grade("Math", 90)
student1.add_grade("English", 85)
student2.add_grade("Math", 80)
student2.add_grade("English", 88)

# Add students to the classroom
classroom.add_student(student1)
classroom.add_student(student2)

# Display all students
classroom.display_students()

# Get average grade of a student
print(f"Alice's average grade: {classroom.get_student_average('Alice')}")
print(f"Bob's average grade: {classroom.get_student_average('Bob')}")

# Get class average for a subject
print(f"Class average for Math: {classroom.get_class_average('Math')}")
print(f"Class average for English: {classroom.get_class_average('English')}")
