#access control
#author jbc
#last updated 8/27/2025
#this app shows how access control is implemented


students = ("James", "Peter", "Julie", "Jake")

Username = input("Please enter User or Admin")

def updateList(name):
    if Username == "Admin":
        students.append(name)
        print(students)
    else:
        print("Only admins can add students to the list")

name = input("Please enter student name to add to the list.")

updateList()
