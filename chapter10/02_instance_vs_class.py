class  Employee:
       name= "Anuj" #this is a class attribute
       language = "Python"
       salary = 120000
       
anuj = Employee()
anuj.name = "anuj" # this is instance atrribute
anuj.language = "Javascript"
print(anuj.name, anuj.language, anuj.salary)

rohan = Employee()
rohan.name = "rohan robinson"
rohan.language = "C++"
print(rohan.name , rohan.salary , rohan.language)
