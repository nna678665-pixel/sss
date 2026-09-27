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

def main():
    while True:
        result = login(admin_lists, students)

        if result == "Admin":
            student_menu(students)
        elif result == "Teacher":
            teacher_menu(students)
        elif isinstance(result, tuple) and result[0] == "Student":
            student_data = result[1]
            print(f"\nWelcome to Student View, {student_data['Name']}!")
            # Once you build student_portal_sms.py, you'll call its menu here!
        elif result is None:
            print("System shutting down. Goodbye!")
            break
if __name__ == "__main__":
    print("MAIN_SYSTEM.PY STARTED")

    while True:
        student_menu(students)
        try:
            options = int(input("Enter option to active application: "))
        except ValueError:
            print("Invalid Options. Please enter a valid number(1-6)")
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
            student_attendance(students)

        elif options == 7:
            print("======================================================")
            print("Thank you for using our application!")
            break



        else:
            print("Invalid Options Please choose a number between 1 and 6.")