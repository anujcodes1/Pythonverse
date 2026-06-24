class  Employee:
       name= "Anuj" #this is a class attribute
       language = "Python"
       salary = 120000
       
       def getInfo(self):
           print(f"The language is {self.language}. The salary is {self.salary}")
           
       @staticmethod
       def greet():
           print("Good morning")
        
       
anuj = Employee()
anuj.name = "anuj" # this is instance atrribute
anuj.greet()
anuj.getInfo()
#Employee.getInfo(anuj)

