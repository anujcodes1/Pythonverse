class  Employee:
       name= "Anuj" #this is a class attribute
       language = "Python"
       salary = 120000
       
       def __init__(self , name, salary, language): #dunder method which is automatically called
           self.name = name
           self.salary= salary
           self.language = language
           
           
           print("I am creating object")
       
       def getInfo(self):
           print(f"The language is {self.language}. The salary is {self.salary}")
           
       @staticmethod
       def greet():
           print("Good morning")
        
       
anuj = Employee("anuj", 150000 , "javascript")
anuj.name = "anuj" # this is instance atrribute
anuj.greet()
anuj.getInfo()
#Employee.getInfo(anuj)

