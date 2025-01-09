class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Grades:")
        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")

    def calculate_average(self):
        if self.grades:
            average = sum(self.grades.values()) / len(self.grades)
            return average
        else:
            return 0

name = input("Enter student's name: ")
age = int(input("Enter student's age: "))

grades = {}
subjects = ['Hindi', 'English', 'Maths', 'Science', 'History', 'Geography']
for subject in subjects:
    grade = int(input(f"Enter grade for {subject}: "))
    grades[subject] = grade

student = Student(name, age, grades)

print("\nStudent Details:")
student.display_details()
print(f"Average Grade: {student.calculate_average():.2f}")
