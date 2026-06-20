word = "Donkey"

with open("chapter9/practiceset_09/file.txt", "r") as f:
    content = f.read()
    
    

contentNew = content.replace(word, "####")

with open("chapter9/practiceset_09/file.txt", "w") as f:
     f.write(contentNew)