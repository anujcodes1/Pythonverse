class student:
    name = "Anuj"
    
s1 = student()
print(s1.name)

s2 = student()
print(s2.name)


class student:
    # default constructor
    def __init__(self):
        pass
    college_name = "ABC College"
    name = "anjaan"  #class attribute
    
    #parameterized constructor
    def __init__(self , fullname , marks):
        self.name = fullname  #object attribute > class attribute
        self.marks = marks
        print("adding new student in database")
    
s1 = student("arjun",56)
print(s1.name , s1.marks , s1.college_name)
s2 = student("abhimanyu",65)
print(s2.name, s2.marks)


class student:

    college_name = "ABC College"
    name = "anjaan"  #class attribute
    
    #parameterized constructor
    def __init__(self , fullname , marks):
        self.name = fullname  #object attribute > class attribute
        self.marks = marks
        print("adding new student in database")
        
    def welcome(self):
        print("welcome student")
        
    def get_marks(self):
        return self.marks
    
s1 = student("arjun",56)
print(s1.name)
print(s1.college_name)
s1.welcome()
print(s1.get_marks())

class car:
    color = "Blue"
    model = "Tata"
    
car1 = car()
print(car1.color)
print(car1.model)


class student:
    def __init__(self, marks):
        self.marks1 = marks
        self.marks2 = marks
        self.marks3= marks
        print("The avg marks is")
        
    def avg(a,b,c):
        d = (a+b+c)/3
        print(d)
        
        
a=int(input("Enter your marks1"))
b=int(input("Enter your marks2"))
c=int(input("Enter your marks3"))
student.avg(a,b,c)


class student:
    def __init__(self, name, marks):
      self.name = name
      self.marks= marks
       
    @staticmethod  #decorator  
    def hello():
        print("hello")
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi" ,self.name , "your avg score is :", sum/3 )
    
s1= student("anuj",[20,16,30])
s1.get_avg()
s1.hello()


class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
        
    #debit
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balance=", self.get_balance())
    
    
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("total balance=", self.get_balance())
        
        
    def get_balance(self):
        return self.balance
        
    
acc1 = Account(2345,10000)
acc1.debit(1000)
acc1.credit(500)
acc1.debit(10000)
acc1.credit(34532)

