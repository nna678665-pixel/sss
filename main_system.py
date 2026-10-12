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
from auth_system import register_user, login
from export_excel import export_students_to_excel

def admin_dashboard():
    while True:
        student_menu(students)
        try:
            options = int(input("Enter option: "))
        except ValueError:
            print("Please enter a valid number.")
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
            break


def student_view(student_data):
    while True:
        print("\n================ STUDENT PORTAL ================")
        print(f"Student ID : {student_data.get('Id')}")
        print(f"Name       : {student_data.get('Name')}")
        print(f"Course     : {student_data.get('Students Course', 'N/A')}")
        print(f"Attendance : {student_data.get('Attendance', 'No records yet')}")
        
        scores = student_data.get("Scores")
        if not scores:
            print("Scores     : No scores recorded yet.")
        else:
            print("Scores     :")
            total = 0
            for subject, mark in scores.items():
                print(f"  • {subject:<23}: {mark}/100")
                total += mark
            avg = total / len(scores)
            print("  ---------------------------------")
            print(f"  Total Score              : {total}")
            print(f"  Average                  : {avg:.2f}")

        print("================================================")
        print("1. Log Out")
        if input("Select option: ") == "1":
            break


def main():
    while True:
        print("\n================ SCHOOL MANAGEMENT PORTAL ================")
        print("1. Register an Account (Admin / Teacher)")
        print("2. Login")
        print("3. Export Records to Excel")
        print("4. Exit Application")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            register_user()

        elif choice == "2":
            auth_result = login(students)
            if auth_result == "Admin":
                admin_dashboard()
            elif auth_result == "Teacher":
                student_attendance(students)
            elif isinstance(auth_result, tuple) and auth_result[0] == "Student":
                student_view(auth_result[1])

        elif choice == "3":
            export_students_to_excel(students)

        elif choice == "4":
            print("Shutting down system. Goodbye!")
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()