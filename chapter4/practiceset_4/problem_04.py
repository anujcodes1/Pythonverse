#Write a program to sum a list with 4 numbers. 
numbers = []
num1 = int(input("Enter the first number: "))
numbers.append(num1)
num2 = int(input("Enter the second number: "))
numbers.append(num2)
num3 = int(input("Enter the third number: "))
numbers.append(num3)
num4 = int(input("Enter the fourth number: "))
numbers.append(num4)
total = sum(numbers)
print("The sum of the numbers is:", total)
