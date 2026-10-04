from students_register_sms import (
    students,
    student_menu,
    add_student,
    search_students,
    update_students,
    delete_students,
    show_student
)

from Teacher_sms import student_attendance

from auth_system import login

admin_lists = {"Admin": "1234", "Teacher": "123456"}
def admin_dashboard():
    while True:
        student_menu(students)
        try:
            options = int(input("Enter option to activate application: "))
        except ValueError:
            print("Invalid Option. Please enter a valid number (1-7).\n")
            continue

        if options == 1:
            add_student()

        elif options == 2:
            show_student()

        elif options == 3:
            search_students()

        elif options == 4:
            update_students()

        elif options == 5:
            delete_students()

        elif options == 6:
            print("\nReturning to Login Portal...")
            break
        else:
            print("Invalid Option! Please choose a number between 1 and 7.\n")


def student_view(student_data):
    while True:
        print("\n================ STUDENT PORTAL ================")
        print(f"Student ID : {student_data.get('Id')}")
        print(f"Name       : {student_data.get('Name')}")
        print(f"Course     : {student_data.get('Course', 'N/A')}")
        print(f"Attendance : {student_data.get('Attendance', 'No records yet')}")
        print("================================================")
        print("1. Log Out")
        scores = student_data.get("Scores")
        if not scores:
            print("Scores     : No scores recorded yet.")
        else:
            print("Scores: ")
            for subject, mark in scores.items():
                print(f"{subject: <25}: {mark / 100}")
        choice = input("Select option: ")
        if choice == "1":
            print("Logging out...\n")
            break
        else:
            print("Invalid option! Press 1 to Log Out.")


def main():
    while True:
        result = login(admin_lists, students)

        if result == "Admin":
            admin_dashboard()

        elif result == "Teacher":
            # Directs teacher straight to attendance
            student_attendance(students)

        elif isinstance(result, tuple) and result[0] == "Student":
            # result is ("Student", found_student)
            student_data = result[1]
            student_view(student_data)

        elif result is None:
            print("\n======================================================")
            print("Thank you for using our application! System shutting down.")
            print("======================================================")

            break


if __name__ == "__main__":
    print("MAIN_SYSTEM.PY STARTED")
    main()