class Programmer:
    company = "Microsoft"
    def __init__(self, name , age):
        self.name = name
        self.age= age
        
        
info = Programmer("Arjun", 23)
print(info.name , info.age, info.company)
info = Programmer("anuj" , 22)
print(info.name , info.age, info.company)
info = Programmer("Aarav",20)
print(info.name , info.age, info.company)
    