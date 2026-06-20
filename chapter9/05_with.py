f = open("chapter9/file.txt")
print(f.read())
f.close()

# The ssame can be wriiten using with statement like this:
with open("file.txt") as f:
    print(f.read())
    
# you dont have to explicity close the file