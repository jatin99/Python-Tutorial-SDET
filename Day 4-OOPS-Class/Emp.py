class Employee: 
    companyName = "Infosys"

    def __init__(self, name,designation):
        self.name = name
        self.designation = designation


    def sign_in(self):
        print(self.name , "Signed in!! ")
    

    def __str__(self):
        return f"Employee name ={self.name} designation = {self.designation} companyName= {Employee.companyName}" 

emp1 = Employee("Pravin", "QA")
emp1.sign_in()
emp2 = Employee("Poonam", "Dev")
emp2.sign_in()
print(emp1)

print(emp2)

