
marks1 = int(input("Enter the marks of subject1: "))
marks2 = int(input("Enter the marks of subject2: "))
marks3 = int(input("Enter the marks of subject3: "))

total = marks1 + marks2 + marks3

if total>=40:
    print("Student is passed")
else:
    print("Student is failed")
    
if marks1<33:
    print("student is failed in subject1")
elif(marks2<33):
    print("student is failed in subject2")
else:
    print("Student is faiiled in subject3")