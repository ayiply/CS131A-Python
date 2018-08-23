#CS131A - Spring 2018
#Andy Y. Ly 
#4/14/2018
#studentObject.py 

class Student:
  name = None
  address = None
  city = None
  state = None
  zip_code = None
  student_id = None
  gpa = None

def inputStudent(y):
  print("Enter name: ")
  y.name = input()
  print("Enter address: ")
  y.address = input()
  print("Enter city: ")
  y.city = input()
  print("Enter state: ")
  y.state = input()
  print("Enter zip code: ")
  y.zip_code = input()
  print("Enter student id: ")
  y.student_id = input()
  print("Enter gpa: ")
  y.gpa = input()

def outputStudent(x):
  print("Name:" + x.name)
  print("Address: " + x.address)
  print("City: " + x.city)
  print("State: " + x.state)
  print("Zip Code: " + x.zip_code)
  print("Student ID: " + x.student_id)
  print("GPA :" + x.gpa)
  
#a, b, c are Student objects, which gets input from inputStudent method
a= Student()
inputStudent(a)
b= Student()
inputStudent(b)
c= Student()
inputStudent(c)

#passes arguments from a,b and c to outputStudent method.
outputStudent(a)
outputStudent(b)
outputStudent(c)