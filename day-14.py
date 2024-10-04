'''
# Day - 14:
'''

# Instance Variables vs Class Variables

class emp:
    company = "FIS"                     # Class Variable
    no_emp = 0
    def __init__(self,name):
        self.name = name                # Instance Variables
        self.hike = 10                  # Instance Variables
        emp.no_emp += 1
    
    def showDetails(self):
        print(f"My Name is {self.name} from {self.company} and have got a total hike of {self.hike}% having a total of {self.no_emp} employees\n")


emp1 =emp("Pradyumna")

emp1.showDetails()
# emp.showDetails(emp1) # this is equivalent to above method call
print(emp.company)

emp2 = emp("Harry")
emp2.hike = 12
emp2.company = 'Apple'
emp2.showDetails()

# Class Methods

class Employee:
    company = "FIS"
    
    def show(self):
        print(f"My Name is {self.name} and I'm currently working at {self.company}\n")

    @classmethod
    def changeCompany(cls, newcompany):  # here cls is like an instance of class Employee
        cls.company = newcompany        # which takes class variable and changes it's value in this particular instance
        print(f"I've now switched to {cls.company}")
    

e1 = Employee()
e1.name = "Pradyumna"
e1.show()

e1.changeCompany("Content Stack")
e1.show()

# Even we change the company name to "Content Stack" from "FIS"
# It won't change the value to class variable until we use @classmethod decorator
print(Employee.company)  

print("\n")
# Class Methods as alternate constructors

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromstring(cls,string):
        name, age = string.split("-")
        return cls(name, int(age))
    
    def showDet(self):
        print(f"My name is {self.name} agged {self.age}")

    
p1 = Person("Orry", 31)
p1.showDet()

string = "Borry-32"
p2 = Person.fromstring(string)
p2.showDet()



