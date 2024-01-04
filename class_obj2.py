class student:
    count=0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:",self.name,"\nAge:",self.age)
obj=student("Hanshika Anchan",18)
obj.display()