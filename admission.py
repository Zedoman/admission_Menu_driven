import time

# =To store student information
students = []

# Function to generate admission number
def generate_admission_number():
    timestamp = int(time.time())  # Current timestamp
    admission_number = f"A{timestamp}"
    return admission_number

# Function to add a new student
def add_student():
    admission_number = generate_admission_number()
    name = input("Enter Name: ")
    phone_num = input("Enter Phone Number: ")
    adhaar_num = input("Enter Aadhaar Number: ")
    address = input("Enter Address: ")

    student = {
        'Admission Number': admission_number,
        'Name': name,
        'Phone Number': phone_num,
        'Aadhaar Number': adhaar_num,
        'Address': address
    }

    students.append(student)
    print(f"Student added successfully! Admission Number: {admission_number}")


#Function to show all students
def show_students():
    for student in students:
        print(student)

# Function to modify student data
def modify_student():
    admission_number = input("Enter Admission Number to modify: ")
    for student in students:
        if student['Admission Number'] == admission_number:
            # Modify data except Admission Number
            student['Name'] = input("Enter new Name: ")
            student['Phone Number'] = input("Enter new Phone Number: ")
            student['Aadhaar Number'] = input("Enter new Aadhaar Number: ")
            student['Address'] = input("Enter new Address: ")
            print("Student data modified successfully!")
            return
    print("Student not found!")

# Function to delete a student
def delete_student():
    admission_number = input("Enter Admission Number to delete: ")
    for student in students:
        if student['Admission Number'] == admission_number:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")

# Function to search for a student
def search_student():
    admission_number = input("Enter Admission Number to search: ")
    for student in students:
        if student['Admission Number'] == admission_number:
            print(student)
            return
    print("Student not found!")

# Main menu
while True:
    print("\nAdmission System Menu:")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Modify Student Data")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        modify_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        search_student()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
