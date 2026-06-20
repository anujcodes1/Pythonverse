# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  



words = ["Donkey" , "bad" , "ganda"]

with open("chapter9/practiceset_09/file.txt", "r") as f:
    content = f.read()
    
    
for word in words:
    
    content = content.replace(word, "#" * len(word))

with open("chapter9/practiceset_09/file.txt", "w") as f:
     f.write(content)