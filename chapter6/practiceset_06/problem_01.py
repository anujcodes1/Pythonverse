#Write a program to find the greatest of four numbers entered by the user. 

a = int(input("Enter the number 1"))
b = int(input("Enter the number 2"))
c = int(input("Enter the number 3"))
d = int(input("Enter the number 4"))

if(a>b and a>c and a>d):
    print("Greatest number is : ", a)
elif(b>a and b>c and b>d):
    print("Greatest number is : ", b)
if(c>a and c>b and c>d):
    print("Greatest number is : ", c)
if(d>a and d>b and d>c):
    print("Greatest number is : ", d)