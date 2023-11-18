class Emp:
    def __init__(self, username): #instance attribute
        self.username=username
    
    def getuserName(self):
        print(self.username)


emp = Emp("jatin")

emp.getuserName()