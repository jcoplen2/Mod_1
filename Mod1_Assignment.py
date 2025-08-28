#access control
#author jbc
#last updated 8/27/2025
#this app shows how access control is implemented


students = ["James", "Peter", "Julie", "Jake"]

Username = input("Please enter User or Admin: ")

def updateList():
    if Username == "Admin":
        students.append(name)
        print("List updated successfully")
        print(students)
    else:
        print("You do not have permission for this.")

name = input("Please enter student name to add to the list: ")

updateList()
