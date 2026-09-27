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
# if __name__ == "__main__":
#     student_attendance(students)



# BUG: Calling functions or running while-loops out in the open at the file level
# means they run IMMEDIATELY when this file is imported by another script.
# When 'main_system.py' imports this file, it freezes here before main even starts!
# FIX: Wrap standalone test code inside: if __name__ == "__main__":

# student_attendance(students)  # <-- WRONG: Runs during import!

# while True:  # <-- WRONG: Freezes main_system.py during import!
#     options = int(input("Enter Option to active program: "))


# def Weekly_Students():
    # BUG: Checking 'if chose == 1:' BEFORE asking the user for 'chose' below!
    # Python executes from top to bottom, so 'chose' does not exist yet.
    # CRASH: UnboundLocalError: cannot access local variable 'chose' where it is not associated with a value
    # FIX: Ask for user input FIRST, then check the value with 'if'.
    
    #if chose == 1:
        # ...
    #chose = int(input("Enter Chose to Access application: "))  # <-- Too late!


# def Weekly_Students():
   # ...
    # BUG: Calling 'Weekly_Students()' inside itself with no condition or return
    # creates an endless function loop that eats up Python's memory.
    # CRASH: RecursionError: maximum recursion depth exceeded
    # FIX: Do NOT use recursion for menus. Use a standard 'while True:' loop instead.
   # Weekly_Students()  # <-- Dangerous self-call!


# MISTAKE: Duplicate option numbers in the menu display.
# Users will not know what number to type to delete attendance.
# FIX: Number options sequentially (1, 2, 3, 4, 5).

# print("3.Search for student Attdendance")  #[cite: 4]
# print("3.Detelt Student Attdendance")      # <-- Should be 4![cite: 4]