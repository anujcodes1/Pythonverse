class Employee:
    b = 99
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a class a is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]    
        
a = Employee()

b = 45
a.name = "Anuj Mishra"

print(b)
print(a.name)
print(a.fname)
print(a.lname)