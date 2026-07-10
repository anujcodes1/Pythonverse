class calculator:
    
    def __init__(self , num1 ):
        self.num1 = num1
        
    def square(self):
        print(f"The square is {self.num1*self.num1}")
        
    def cube(self):
        print(f"The cube is {self.num1**self.num1}")
        
    def sqrt(self):
        print(f"The squareroot of a number is{self.num1**0.5}")
        
        
a= calculator(4)
a.square()
a.cube()
a.sqrt()


        
        
        
