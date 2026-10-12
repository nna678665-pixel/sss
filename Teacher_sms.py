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
            print("========================Students Attendance Management Menu==================")
            print("1. Daily students Attendance")
            print("2. Weekly students Attendance")
            print("3. Back")
            try:
                ad = int(input("Enter choice to activate program: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            match ad:
                case 1:
                    print("=============Daily students Attendance===========: ")
                    weekly_students(students_list, mode="Daily")
                case 2:
                    print("=============Weekly students Attendance===========")
                    weekly_students(students_list, mode="Weekly")
                case 3:
                    continue

        elif chose == 2:
            student_scores(students_list)  # <-- Calls score management!

        elif chose == 3:
            print("Returning to Main Menu...")
            break
        else:
            print("Please choose 1, 2, or 3.")


def student_scores(students_list):
    while True:
        print("\n================== Student Scores Management ==================")
        print("1. Submit Student Scores")
        print("2. View Students Score Board")
        print("3. Back")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            print("\n================== Submit Student Scores ==================")
            if not students_list:
                print("No students enrolled yet.")
            else:
                subject = input("Enter Subject Name (e.g. Coding Skill, Understanding Workflow): ")
                for student in students_list:
                    if "Scores" not in student:
                        student["Scores"] = {}

                    while True:
                        try:
                            score = float(input(f"Enter {subject} score for {student['Name']} (0-100): "))
                            if 0 <= score <= 100:
                                student["Scores"][subject] = score
                                break
                            else:
                                print("Score must be between 0 and 100!")
                        except ValueError:
                            print("Please enter a valid numeric score.")

                print(f"Scores for {subject} submitted successfully!")

        elif choice == 2:
            print("\n============ Students Scores Board ============")
            if not students_list:
                print("No students enrolled yet.")
            else:
                for student in students_list:
                    print("----------------------------------------------------------")
                    print(f"Student ID   : {student.get('Id')}")
                    print(f"Student Name : {student.get('Name')}")
                    
                    scores = student.get("Scores")
                    if not scores:
                        print("Score Status : No scores recorded yet.")
                    else:
                        print("--- Subject Scores ---")
                        total = 0
                        for subject, mark in scores.items():
                            print(f"  • {subject:<25} : {mark}/100")
                            total += mark
                        
                        avg = total / len(scores)
                        print(f"  Total Score : {total}")
                        print(f"  Average     : {avg:.2f}")
                print("----------------------------------------------------------")

        elif choice == 3:
            print("Returning to Attendance Menu...")
            break
        else:
            print("Please choose 1, 2, or 3.")


def weekly_students(students_list , mode="Daily"):
    while True:
        print(f"\n================ Students {mode} Attendance Management ================")
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
            print(f"================== Submit {mode} Students Attendance ==================")
            if not students_list:
                print("No students enrolled yet.")
            else:
                if mode == "Daily":
                    date = input("Enter Daily Session (e.g. Morning, Afternoon): ")
                else:
                    date = input("Enter Weekly Session (e.g. Week 1, Week 2): ")

                for student in students_list:
                    if "Attendance" not in student:
                        student["Attendance"] = {}

                    status = input(f"Enter status for {student['Name']} (Present/Absent): ")
                    student["Attendance"][date] = status
                print("Attendance submitted successfully!")

                # date = input("Enter Study Session (e.g. Session 1, Morning, Week 1): ")
                # for student in students_list:
                #     # Make sure the student has an Attendance dictionary
                #     if "Attendance" not in student:
                #         student["Attendance"] = {}
                    
                #     status = input(f"Enter status for {student['Name']} (Present/Absent): ")
                #     student["Attendance"][date] = status
                # print("Attendance submitted successfully!")

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
            print(f"\n================== Delete {mode} Student Attendance ==================")
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

if __name__ == "__main__":
    # Test harness when running Teacher_sms.py directly
    mock_students = [
        {"Id": "1", "Name": "Alice", "Course": "Python"},
        {"Id": "2", "Name": "Bob", "Course": "Python"}
    ]
    student_attendance(mock_students)

