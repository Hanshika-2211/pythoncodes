print(""" STUDENT ADMIT  
------------------""")
class Student:
    def __init__(self): #This is used 
        self.name = input("Enter the name: ")
        self.age = int(input("Enter the age: "))
        self.department=input("Enter your department(PGDM/BTech):")
        Student.count=+1
    def display(self):
        print("Name : ",self.name,"\nAge :",self.age,"\nDepartment :",self.department)
        print(Student.count)
obj1 = Student()
obj1.display()
Student.count