#if elif else ladder concept

age = int(input("Enter your age pelase: "))

if (age>=18):
    print("You are not eligible for voting")
elif(age==0):
    print("You are entering zero whic is not a valid age")
elif(age<0):
    print("You are entering negative value")
else:
    print("You are eligible for voting")