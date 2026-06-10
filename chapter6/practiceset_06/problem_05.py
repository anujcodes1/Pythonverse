#Write a program which finds out whether a given name is present in a list or not.

list=["amar", "anuj", "arjun", "akash", "anay"]
name = input("Enter the name please: ")

if (name in list):
    print("Name is present in this list")
else:
    print("Name is not  present in this list")