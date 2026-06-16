#  Write a program using functions to find greatest of three numbers.

# def greatnum():
    
#     a = int(input("Enter your first number: "))
#     b = int(input("Enter your second number: "))
#     c = int(input("Enter your third number: "))
    
#     if(a>b and c>c ):
#         print("a is greatest number: ", a)
#     elif(b>a and  b>c):
#         print("b is greatest number: ", b)
#     else:
#         print("c is greatest number: ", c)
        
# greatnum()


def greatest(a, b, c):
    if(a>b and b>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))
print(greatest(a, b, c))