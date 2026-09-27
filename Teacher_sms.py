from students_register_sms import students


def student_attendance(students_list):
    print("\n================ Attendance Menu ================")
    print("1. Students Daily Attendance Management")
    print("2. Student Score Management")
    print("3. Back to Main Menu")

    try:
        chose = int(input("Enter choice to access: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if chose == 1:
        weekly_students(students_list)
    elif chose == 2:
        print("Score management coming soon!")
    elif chose == 3:
        ...


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
            print("================== Weekly Student Attendance ==================")
            if not students_list:
                print("No students enrolled yet.")
            else:
                for student in students_list:
                    print(student)
        elif choice == 5:
            break
        else:
            print("Option not implemented yet.")


# This block ONLY runs if you run Teacher_sms.py directly,
# but it will NOT interfere when imported into main_system.py!
if __name__ == "__main__":
    student_attendance(students)