students = {}  # This will store student information.

def add_student(student_id, name, age, grades):
    students[student_id] = {"name": name, "age": age, "grades": grades}
    print(f"Student {name} added successfully!")



def view_student(student_id):
    if student_id in students:
        print(f"Student ID: {student_id}, Data: {students[student_id]}")
    else:
        print("Student not found.")




def update_student(student_id, name=None, age=None, grades=None):
    if student_id in students:
        if name:
            students[student_id]["name"] = name
        if age:
            students[student_id]["age"] = age
        if grades:
            students[student_id]["grades"] = grades
        print(f"Student {student_id} updated successfully!")
    else:
        print("Student not found.")




def delete_student(student_id):
    if student_id in students:
        deleted_student = students.pop(student_id)
        print(f"Student {deleted_student['name']} deleted successfully!")
    else:
        print("Student not found.")



while True:
    print("\nChoose an option:")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")



    if choice == "1":  #  TO Add a new student
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grades = input("Enter student grades (comma-separated): ").split(",")
        add_student(student_id, name, age, grades)



    elif choice == "2":  # View a student's information
        student_id = input("Enter student ID: ")
        view_student(student_id)

    elif choice == "3":  # Update student information
        student_id = input("Enter student ID: ")
        print("Leave fields blank if you don't want to update them.")
        name = input("Enter new name (or press Enter to skip): ")
        age = input("Enter new age (or press Enter to skip): ")
        grades = input("Enter new grades (comma-separated, or press Enter to skip): ")
        update_student(student_id, name or None, int(age) if age else None, grades.split(",") if grades else None)


    elif choice == "4":  # Delete a student
        student_id = input("Enter student ID: ")
        delete_student(student_id)
        

    elif choice == "5":  # Exit the program
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
