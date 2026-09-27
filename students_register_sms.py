students = []

def student_menu(student_list):
    print("=================== Students Information ====================")
    print("1. Add Students Information")
    print("2. View Students Information")
    print("3. Search Students Information")
    print("4. Update Students Information")
    print("5. delete Students Information")
    print("6. Exit Application")


def validate_phone(phone):
    if phone.isdigit() and phone.startswith("0") and len(phone) in (9, 10):
        return True
    else:
        return False


def add_student():
    print("=================Add Students Information")

    student_name = input("Enter Student Name: ")

    # 1. Check whether ID contains only digits and is not duplicated
    while True:
        student_id = input("Enter Students ID: ")
        
        while not student_id.isdigit():
            print("Please Enter a Valid ID. Students ID can't contain alphabets!")
            student_id = input("Enter Students ID: ")

        dup = False
        for student in students:
            if student["Id"] == student_id:
                dup = True
                print("This Student ID is really exists!")
                break

        if not dup:
            break

    # 2. Check age
    while True:
        try:        
            students_age = int(input("Enter Student Age: ")) 
            if students_age <= 0:
                print("Students is to young to studay")
            else:     
                break
        except ValueError:
            print("Age can't be use with aplhabet!")
        
    # 3. Check course
    while True:
        student_course = input("Enter the course that Student what to learn: ")
        if student_course.strip():
            break
        print("Please Enter a Valid Course!")
    
    enrollment_status = input("Enter enrollment Status: ")
    date_of_birth = input("Data of Birth: ")
    tuition_fee = input("Studnets Tuition Fee: $")

    # 4. Check phone number (outside course check so it never crashes)
    while True:
        student_phone = input("Enter Studnet Phone Number: ")
        if validate_phone(student_phone):
            print("Phone number is valid!")
            break
        else: 
            print("Invalid phone number!")
                        
    students.append({
        "Name": student_name,
        "Id": student_id,
        "Age": students_age,
        "Students Course": student_course,
        "Enrollment Status": enrollment_status,
        "Data of Birth": date_of_birth,
        "Tuition_Fee": tuition_fee,
        "PhoneNumber": student_phone
    })
    print("Stundent Information has Add")


def show_student():
    if not students:
        print("There no students in the systems yet!")
    else:
        for student in students:
            print("==================All Student Information=================")
            print(f"Student Name: {student['Name']}")
            print(f"Student ID: {student['Id']}")
            print(f"Student Age: {student['Age']}")
            print(f"Students Course: {student['Students Course']}")
            print(f"Enrollment Status: {student['Enrollment Status']}")
            print(f"Student Date of Brith: {student['Data of Birth']}")
            print(f"Student Tuition_Fee$: {student['Tuition_Fee']}")
            print(f"Student PhoneNumber: {student['PhoneNumber']}")
            print("==========================================================")


def search_students():
    if not students:
        print("There has not students in our system yet!")
    else:
        print("==================Search Student Information by================")
        print("1.Search Students by ID")
        print("2.Search Students by Name")
        print("3.Search Students by Course")
        print("4.Search Students by PhoneNumber")

        try:
            option = int(input("Enter Search Options: "))
        except ValueError:
            print("Invalid input!")
            return

        match option:
            case 1:
                search = input("Search Students Informations by ID: ")
                found = False
                for student in students:
                    if search == student["Id"]:
                        print("=================Student Information==================================")
                        print(f"Student Name: {student['Name']}")
                        print(f"Student ID: {student['Id']}")
                        print(f"Student Age: {student['Age']}")
                        print(f"Student Course: {student['Students Course']}")
                        print(f"Enrollment Status: {student['Enrollment Status']}")
                        print(f"Student Date of Brith: {student['Data of Birth']}")
                        print(f"Student Tuition_Fee$: {student['Tuition_Fee']}")
                        print(f"Student PhoneNumber: {student['PhoneNumber']}")
                        found = True
                        break
                if not found:
                    print(f"The Students ID {search} is not in our system")

            case 2:
                search = input("Search Students Information by Name: ")
                found = False
                for student in students:
                    if search == student["Name"]:
                        print("=================Student Information==================================")
                        print(f"Student Name: {student['Name']}")
                        print(f"Student ID: {student['Id']}")
                        print(f"Student Age: {student['Age']}")
                        print(f"Student Course: {student['Students Course']}")
                        print(f"Enrollment Status: {student['Enrollment Status']}")
                        print(f"Student Date of Brith: {student['Data of Birth']}")
                        print(f"Student Tuition_Fee$: {student['Tuition_Fee']}")
                        print(f"Student PhoneNumber: {student['PhoneNumber']}")
                        found = True
                        break
                if not found:
                    print(f"The Student Name {search} is not in our system")

            case 3:
                search = input("Search Students Information by Course: ")
                found = False
                for student in students:
                    if search == student["Students Course"]:
                        print("=================Student Information==================================")
                        print(f"Student Name: {student['Name']}")
                        print(f"Student ID: {student['Id']}")
                        print(f"Student Age: {student['Age']}")
                        print(f"Student Course: {student['Students Course']}")
                        print(f"Enrollment Status: {student['Enrollment Status']}")
                        print(f"Student Date of Brith: {student['Data of Birth']}")
                        print(f"Student Tuition_Fee$: {student['Tuition_Fee']}")
                        print(f"Student PhoneNumber: {student['PhoneNumber']}")
                        found = True
                        break
                if not found:
                    print(f"The Student Course {search} is not in our system")

            case 4:
                search = input("Search Students by PhoneNumber: ")
                found = False
                for student in students:
                    if search == student["PhoneNumber"]:
                        print("=================Student Information==================================")
                        print(f"Student Name: {student['Name']}")
                        print(f"Student ID: {student['Id']}")
                        print(f"Student Age: {student['Age']}")
                        print(f"Student Course: {student['Students Course']}")
                        print(f"Enrollment Status: {student['Enrollment Status']}")
                        print(f"Student Date of Brith: {student['Data of Birth']}")
                        print(f"Student Tuition_Fee$: {student['Tuition_Fee']}")
                        print(f"Student PhoneNumber: {student['PhoneNumber']}")
                        found = True
                        break
                if not found:
                    print(f"The Student PhoneNumber {search} is not in our system")


def update_students():
    if not students:
        print("There has not students in our system yet!")
    else:
        print("====================Update Students Information by=====================================")
        print("1.Students ID")
        print("2.Students Name")
        print("3.Students Course")
        print("4.Students PhoneNumber")

        try:
            choise = int(input("What Information you what to update: "))
        except ValueError:
            print("Invalid input!")
            return

        match choise:
            case 1:
                print("==================Update Students ID======================")
                search = input("Comform Students ID to upate: ")
                found = False
                for student in students:
                    if search == student["Id"]:
                        print("==================Enter New Student ID===============================================")
                        new_id = input("Enter Students New ID: ")
                        student["Id"] = new_id
                        print("Update Student ID")
                        found = True
                        break
                if not found:
                    print(f"The students ID {search} is not it the system!")

            case 2:
                print("==================Update Students Name======================")
                search = input("Comform Students ID to upate: ")
                found = False
                for student in students:
                    if search == student["Id"]:
                        print("=====================================Enter Student Name================================")
                        new_name = input("Enter New Student name: ")
                        student["Name"] = new_name
                        print("Update Student name")
                        found = True
                        break
                if not found:
                    print(f"The students ID {search} is not it the system!")

            case 3:
                print("==================Update Students Course======================")
                search = input("Comform Students ID to upate: ")
                found = False
                for student in students:
                    if search == student["Id"]:
                        print("=====================================Enter Student Course================================")
                        new_course = input("Enter New Student Course: ")
                        student["Students Course"] = new_course
                        print("Update Student Course")
                        found = True
                        break
                if not found:
                    print(f"The students ID {search} is not it the system!")

            case 4:
                print("==================Update Students PhoneNumber======================")
                search = input("Comform Students ID to upate: ")
                found = False
                for student in students:
                    if search == student["Id"]:
                        print("=====================================Enter Student PhoneNumber================================")
                        new_phone = input("Enter New Student PhoneNumber: ")
                        student["PhoneNumber"] = new_phone
                        print("Update Student PhoneNumber")
                        found = True
                        break
                if not found:
                    print(f"The students ID {search} is not it the system!")


def delete_students():
    if not students:
        print("There has not students in our system yet!")
    else:
        print("============================Enter ID to Delete============================================")
        searchs = input("Enter ID of the Students that you want to delete Information: ")
        found = False

        for student in students:
            if student["Id"] == searchs:
                students.remove(student)
                print("Student information delete")
                found = True
                break

        if not found:
            print(f"The Students ID {searchs} is not in our system")





# First BUG: Putting 'while not student_id.isdigit()' inside 'for student in students:'
# causes a bug when the list is empty: the for-loop never runs, so the digit check never runs!
# FIX: Check if it is a digit FIRST, and check for duplicates in the list SECOND.
# while not student_id.isdigit():
#     print("Please Enter a Valid ID. Students ID can't contain alphabets!")
#     student_id = input("Enter Students ID: ")



# Secondary BUG: 'student_phone' is indented inside the 'else:' block of course validation!
# If the user enters an empty course, Python skips the 'else:' branch,
# meaning 'student_phone' is NEVER created. 
# Down at the bottom, Python crashes with: UnboundLocalError: local variable 'student_phone' referenced before assignment.
# FIX: Pull 'student_phone' out of the 'else:' block and validate each input one by one.
# if not student_course.strip():
#     ...
# else:
#     student_phone = input("Enter Studnet Phone Number: ")  # <-- WRONG INDENTATION


# third BUG MISTAKE: Using double quotes inside double quotes: f"Student Name: {student["Name"]}"
# In Python 3.11 and older, this causes a SyntaxError because Python gets confused where the string ends.
# FIX: Use single quotes inside the curly brackets: {student['Name']}


# for student in students:
    # fourth BUG: If the first student in the list does NOT match the ID, 
    # it immediately prints "ID is not in our system" for EVERY non-matching student!
    # Also, using 'students.remove()' inside a running loop can cause Python to skip elements.
    # FIX: Use a boolean flag like 'found = False', remove the student, and break immediately.
    # if student["Id"] != searchs:
    #     print(f"The Students ID {searchs} is not in our system")
    # else:
    #     students.remove(student)

# case 4:
    # fifth BUG MISTAKE: Copy-paste error from Case 3! 
    # The banner says "Enter Student Course", but the input asks for "Enter New Student PhoneNumber".
    # FIX: Update the text banner to match the input.
    # print("==================Enter Student Course==================")
    # new_phone = input("Enter New Student PhoneNumber: ")


# try:
#     options = int(input("Enter option to active application: "))
# except ValueError:
#     print("Invalid Options. Please enter a valid number(1-6)")
    # Six BUG: Without 'continue' here, Python will keep running down into 'if options == 1:'!
    # If 'options' doesn't exist yet, it crashes with NameError.
    # FIX: Add 'continue' inside the except block so the loop restarts safely.
    # continue