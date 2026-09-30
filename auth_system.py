# from students_register_sms import students
admin_lists = {"Admin": "1234", "Teacher": "123456"}

def login(admin_lists, students):
    print("1.Register as Register")
    print("2.Register as Teacher")
    print("3.Register as student")
    print("4.Exit")

 
    while True:
        chose = int(input("Register as: "))

        match chose:
            case 1:
                print("==========Rigister as a Register======")
                enter_user = input("Enter User Name: ")
                enter_pw = input("Enter Password: ")
                if enter_user == "Admin" and admin_lists.get("Admin") == enter_pw:
                    print("Login Successful")
                    return "Admin"
                else:
                    print("Wrong Password.Pleas Enter again!")
                    #When someone types the wrong password, just print the warning.
                    # Do not ask for enter_user and enter_pw inside else:, because 
                    # those values never get checked. Let the loop run again naturally.
                    # enter_user = input("Enter User Name: ")
                    # enter_pw = int(input("Enter Password: "))
            case 2:
                  print("==========Rigister as a Teacher======")
                  enter_user = input("Enter User Name: ")
                  enter_pw = input("Enter Password: ")
                  if enter_user == "Teacher" and admin_lists.get("Teacher") == enter_pw:
                      print("Login Successful")
                      return "Teacher"
                  else:
                      print("Wrong Password or Worng Username.")
            case 3:
                print("========== Login as a Student ==========")
                enter_id = input("Enter Student ID: ")

                found_student = None
                for student in students:
                    if str(student["Id"]) == str(enter_id):
                        found_student = student
                        break

                if found_student:
                    print(f"Login Successful! Welcome, {found_student['Name']}!")
                    return ("Student", found_student)
                else:
                    print("Student ID not found! Please check and try again.\n")
                      
            case 4:
                print("Exiting...")
                return None 
                             
# login(admin_lists)
# logged_in_role = login(admin_lists)
# print(f"Logged in as: {logged_in_role}")               

        
# At the very bottom of auth_system.py:
if __name__ == "__main__":
    # Test code only runs when executing this file directly
    mock_students = [{"Id": "1", "Name": "Alice", "Course": "Python"}]
    admin_lists = {"Admin": "1234", "Teacher": "123456"}
    res = login(admin_lists, mock_students)
    print(res)

# if str(student["Id"]) == str(enter_id):
#             found_student = student
#             break

#     if found_student:
#         print(f"Login Successful! Welcome, {found_student['Name']}!")
#         # Return both the role and the student's dict so you know WHO logged in!
#         return ("Student", found_student)
#     else:
#         print("Student ID not found! Please check and try again.\n")