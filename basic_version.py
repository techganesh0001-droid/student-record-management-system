students = []

while True:
    print("\n====Student record management sysytem====")
    print("1. Add student record")
    print("2. Display student records") 
    print("3. Search student record")
    print("4. Update student record")
    print("5. Delete student record")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        rollnumber = input("Enter student roll number: ")
        if any(student['roll_number'] == rollnumber for student in students):
            print("Roll number already exists. Please enter a unique roll number.")
            continue
        name = input("Enter student name: ")
        try:
            marks = float(input("Enter student marks: "))
        except ValueError:
            print("Please enter valid marks.")
        continue
        students.append({'roll_number': rollnumber, 'name': name, 'marks': marks})
        print("student added sucessfully")

    elif choice == "2" :
        if len(students) == 0:
            print("no Students records found")
        else:
            print('\n====STUDENT RECORDS====')
            for student in students:
                print(f"Roll Number: {student['roll_number']}, Name: {student['name'].lower()}, Marks: {student['marks']}")
                print("=====================================")

    elif choice == "3":
        search_roll_number = input("Enter the roll number of the student to search: ")
        found = False
        for student in students:
            if student['roll_number'] == search_roll_number:
                print(f"Roll Number: {student['roll_number']}, Name: {student['name'].lower()}, Marks: {student['marks']}")
                found = True
                break
        if not found:
            print("Student record not found.")    

    elif choice == "4":
        update_roll_number = input("Enter the roll number of the student to update: ")
        found = False
        for student in students:
            if student['roll_number'] == update_roll_number:
                new_name = input("Enter new name: ")
                new_marks = float(input("Enter new marks: "))
                student['name'] = new_name
                student['marks'] = new_marks
                print("Student record updated successfully.")
                found = True
                break
        if not found:
            print("Student record not found.")               
    elif choice == "5":
        delete_roll_number = input("Enter the roll number of the student to delete: ")
        found = False
        for student in students:
            if student['roll_number'] == delete_roll_number:
                students.remove(student)
                print("Student record deleted successfully.")
                found = True
                break
        if not found:
            print("Student record not found.")
    elif choice == "6":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
