#Create a function that takes a number and prints its square.

# def square(n):
#     return n** 2

# n = int(input("Enter your number: "))
# print(square(n))

#Create a function that accepts a number and tells whether it is even or odd.

# def num():
#     if n%2==0:
#         print("The number is even")
#     else:
#         print("The number is odd")
        
        
# n = int(input("Enter your number: "))
# print(num())


#Function to Find the Largest of Two Numbers


# def largest(a,b):
#     if(a>b):
#         print("a is greater number",a)
#     else:
#         print("b is greater number", b)
        
# a=int(input("Enter your first number: "))
# b=int(input("Enter your second number: "))

# largest(a,b)

# average of three numbers

# def avg(a,b,c):
#     sum = (a+b+c)/3
#     print("The average of three numbers is: ", sum)



# a=int(input("Enter your first number: "))
# b=int(input("Enter your second number: "))
# c=int(input("Enter your third number: "))
# avg(a,b,c)


#Function to Calculate Simple Interest

# def simple_interest(p,r,t):
#     si = (p * r * t)/100
#     print("The simple interest is: ",si)
#     return si
    
    
# p = int(input("Enter the principal amount: "))    
# r = float(input("Enter the  rate of interest: "))    
# t = int(input("Enter the time: "))    
    
# simple_interest(p,r,t)
    
    
    #. Function to Calculate Perimeter of a Rectangle

# def perimeter(l, w):
#     peri = 2 * ( l + w)
#     print("The perimeter of rectangle is: ",peri) 
#     return peri
    
    
# l = int(input("Enter the length of the rectangle: "))
# w = int(input("Enter the width  of the rectangle: "))
# perimeter(l, w)


#Function to Count Characters in a String

def count_char(string):
    count = 0
    for char in string:
        count += 1
    print("The number of  characters in the string are: ", count)
    
    
    
string = input("Enter your message: ")
count_char(string)






