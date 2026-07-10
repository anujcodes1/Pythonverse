class classy:
     a = "anuj"
     
an = classy()
print(an.a) #prints the class attribute because instance attribute is not present
an.a = "mishra" #instance attribute is set
print(an.a) #prints the instance attribute becuase instance attribute is present
print(classy.a) #prints the class attribute