class Person:
    country = "India"

    def __init__(self, name):
        self.name = name

    def getUserData(self):
        print("User", self.name, Person.country)

    def __str__(self):
        return f"My name is {self.name} and I am from {Person.country}."

p = Person("Jatin")
p.getUserData()

# Class Variable access
print(p.__class__.country)

# Instance Variable access
print(p.name)

# Print using __str__
print(p)
