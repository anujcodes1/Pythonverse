class Employee:     #Base classs
    company = "Apple"
    name = "default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.company}")
        

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all languages her is your language: {self.language}")
    


class Programmer(Employee , Coder):     #derived class , inherited class
    company = "ITC"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
        
        
a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()

print(a.company , b.company)