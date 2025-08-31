#access control
#author jbc
#last updated 8/31/2025
#this app shows how access control is implemented. It provides confidentiality via
#a login. The data integrity is protected by access control. There are no issues
#with availability. 

#create list
students = ["James", "Peter", "Julie", "Jake"]

#Simulate login
Username = input("Please enter User or Admin: ")

#Admin only function
def updateList():
    if Username == "Admin":
        students.append(name)
        print("List updated successfully")
        print(students)
    else:
        print("You do not have permission for this.")

#Student only function
def viewList():
    if Username == "User":
        print("Here is a list of the students:")
        print(students)
    else:
        print("You do not have permission for this.")

#Control access
if Username == "Admin":
    name = input("Please enter student name to add to the list: ")
    updateList()
elif Username == "User":
    viewList()
else:
    print("Invalid Role")

