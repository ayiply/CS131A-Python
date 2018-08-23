#CS131A - Python Programming Asmt 3 - Spring 2018
#Andy Y. Ly
#3/5/2018

#initialize keys in dictionary 'student' to empty string
student = {'first name': '', 'last name': '', 'student_id': ''}
student['first name'] = input("Enter first name: ")
student['last name'] = input("Enter last name: ")
student['student_id'] = input("Enter student_id: ")


# Cast user input to lower-case 'y'
answer = input("add more to the dictionary (Y or y for yes): ").lower()
# Define yes as a set of possible inputs
yes = set(['Y', 'y'])

#While Loop - while answer is in the set "yes"
while answer in yes:
    new_key = input("enter a kind of information to add: ")
    student[new_key] = input("enter the value for the information to add: ")
    answer = input("add more to the dictionary (Y or y for yes): ").lower()

#Print items in the dictionary 'student' keys and values with colon 
for k,v in student.items():
    print(k + ' : ' + v)