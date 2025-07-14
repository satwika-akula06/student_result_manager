

students = []

def add_student():
    name = input("Enter student name: ")
    try:
        Mathematics = int(input("Enter marks in Mathematics: "))
        Science = int(input("Enter marks in Science: "))
        English = int(input("Enter marks in English: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for marks.")
        return

    total = Mathematics + Science + English
    average = total / 3

    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 40:
        grade = 'D'
    else:
        grade = 'F'

    student = {
        'name': name,
        'Mathematics': Mathematics,
        'Science': Science,
        'English': English,
        'total': total,
        'average': average,
        'grade': grade
    }

    students.append(student)
    print(f"Student '{name}' added successfully.\n")

def show_all_results():
    if not students:
        print("No student records found.\n")
        return

    print("\n All Student Results:")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"  Total: {student['total']}")
        print(f"  Average: {student['average']:.2f}")
        print(f"  Grade: {student['grade']}")
        print("-----------")

def show_topper():
    if not students:
        print("No students available to evaluate topper.\n")
        return

    topper = max(students, key=lambda x: x['total'])
    print(f"\n Topper: {topper['name']} with {topper['total']} marks.\n")

def main_menu():
    while True:
        print(" Student Result Management System")
        print("1. Add Student")
        print("2. Show All Results")
        print("3. Show Topper")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            show_all_results()
        elif choice == '3':
            show_topper()
        elif choice == '4':
            print("THANK YOU!")
            break
        else:
            print("Invalid choice. Please enter 1-4.\n")

if __name__ == "__main__":
    main_menu()
