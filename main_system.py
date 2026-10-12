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

admin_lists = {"Admin": "1234", "Teacher": "123456"}
def admin_dashboard():
    while True:
        student_menu(students)
        try:
            options = int(input("Enter option to active application: "))
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
            print("Returning to Main Role Menu...")
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
            print("Scores: ")
            for subject, mark in scores.items():
                print(f"{subject: <25}: {mark}  / 100")
                total = +mark

                avg = total / len(scores)
                print("  ---------------------------------")
                print(f"  Total Score: {total}")
                print(f"  Average: {avg:.2f}")

                
        print("================================================")
        print("1. Log Out")

        choice = input("Select option: ")
        if choice == "1":
            print("Logging out...\n")
            break
        else:
            print("Invalid option! Press 1 to Log Out.")


def main():
    while True:
        print("\n================ LOGIN PORTAL ================")
        print("1. Admin Login")
        print("2. Teacher Login")
        print("3. Student Login")
        print("4. Exit Application")

        role = input("Select Option: ")

        if role == "1":
            user = input("Enter Admin Username: ")
            pwd = input("Enter Password: ")
            if user == "Admin" and pwd == "1234":
                print("Admin login successful!")
                admin_dashboard()
            else:
                print("Invalid Admin credentials!")

        elif role == "2":
            user = input("Enter Teacher Username: ")
            pwd = input("Enter Password: ")
            if user == "Teacher" and pwd == "123456":
                print("Teacher login successful!")
                student_attendance(students)
            else:
                print("Invalid Teacher credentials!")

        elif role == "3":
            s_id = input("Enter your Student ID: ")
            found = next((s for s in students if s["Id"] == s_id), None)
            if found:
                student_view(found)
            else:
                print(f"Student ID '{s_id}' not found in the system.")

        elif role == "4":
            print("Thank you for using our application! System shutting down.")
            break
        else:
            print("Invalid option, please choose 1-4.")

if __name__ == "__main__":
    print("MAIN_SYSTEM.PY STARTED")
    main()