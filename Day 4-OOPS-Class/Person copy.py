class Person:
    country = "India" #attribute 

    def __init__(self, name): #instance variable
        self.name = name
        print("Name is", self.name)
    
    def doSomeWork(self):
        print(self.name , "doing some work..... and is from", Person.country)

   

person = Person("Raj")
person.doSomeWork()
person2 = Person("Charan")
person2.doSomeWork()
print(person2.__class__.country)