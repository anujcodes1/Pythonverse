class  Employee:
       name= "Anuj" #this is a class attribute
       language = "Python"
       salary = 120000
       
anuj = Employee()
anuj.name = "anuj" # this is instance atrribute
print(anuj.name, anuj.language, anuj.salary)

rohan = Employee()
rohan.name = "rohan robinson"
print(rohan.name , rohan.salary , rohan.language)

#Here name is instance attribute and salary and language are class attributes as they directly belong to the class