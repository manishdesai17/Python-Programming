class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def details(self):
        print("Person details : ")
        print("Name : ",self.name)
        print("Age : ",self.age)

    def display(self):
        print(f"Person Inforamtion : Name : {self.name} , Age : {self.age}")

class Employee(Person):
    def __init__(self,name,age,jobRole,salary):
        super().__init__(name,age)
        self.jobRole = jobRole
        self.salary = salary

    def display(self):
        super().display()
        print(f"Job Role : {self.jobRole}, Salary : {self.salary} ")
        
    def details(self):
        print("Employee details : ")
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Job Role : ",self.jobRole)
        print("Salary : ",self.salary)



p = Person("Jay",25)
p.details()
p.display()

e = Employee("Anis",25,"Manager",100000)
e.details()
e.display()