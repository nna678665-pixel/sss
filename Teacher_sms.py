def student_attendance(students_list):
    while True:
        print("\n================ Attendance Menu ================")
        print("1. Students Attendance Management")
        print("2. Student Score Management")
        print("3. Back to Main Menu")

        try:
            chose = int(input("Enter choice to access: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if chose == 1:
            print("========================Attedndance Menu==================")
            print("1.Daily students Attedndance ")
            print("2.Weekly students Attedndance ")

            at = int(input("Enter chose to actiy program: "))
            match at:
                case 1:
                    print("=============Daily students Attedndance===========: ")
                    weekly_students(students_list)
                case 2:
                    print("=============Weekly students Attedndance===========")
        elif chose == 2:
            print("Score management coming soon!")
        elif chose == 3:
            print("Returning to Main Menu...")
            break
        else:
            print("Please choose 1, 2, or 3.")


def weekly_students(students_list):
    while True:
        print("\n================ Students Daily Attendance Management ================")
        print("1. Submit Students Attendance")
        print("2. View Students Attendance")
        print("3. Search for Student Attendance")
        print("4. Delete Student Attendance")
        print("5. Back")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            print("================== Submit Students Attendance ==================")
            if not students_list:
                print("No students enrolled yet.")
            else:
                date = input("Enter date (e.g. 2026-09-27): ")
                for student in students_list:
                    # Make sure the student has an Attendance dictionary
                    if "Attendance" not in student:
                        student["Attendance"] = {}
                    
                    status = input(f"Enter status for {student['Name']} (Present/Absent): ")
                    student["Attendance"][date] = status
                print("Attendance submitted successfully!")

        elif choice == 2:
            print("================== View Students Attendance ==================")
            if not students_list:
                print("No students enrolled yet.")
            else:
                for student in students_list:
                    print(f"ID: {student.get('Id')} | Name: {student.get('Name')} | Attendance: {student.get('Attendance', 'No record')}")

        elif choice == 3:
            print("================== Search Student Attendance ==================")
            search_id = input("Enter Student ID to search: ")
            found = False
            for student in students_list:
                if str(student.get("Id")) == str(search_id):
                    print(f"Name: {student.get('Name')} | Attendance: {student.get('Attendance', 'No record')}")
                    found = True
                    break
            if not found:
                print("Student ID not found.")

        elif choice == 4:
            print("================== Delete Student Attendance ==================")
            delete_id = input("Enter Student ID to clear attendance: ")
            found = False
            for student in students_list:
                if str(student.get("Id")) == str(delete_id):
                    student["Attendance"] = {}
                    print(f"Attendance records cleared for {student.get('Name')}.")
                    found = True
                    break
            if not found:
                print("Student ID not found.")

        elif choice == 5:
            break
        else:
            print("Option not implemented yet.")