name = "Harry"

print(name[name[0:3]])  # output : Har , because it will first evaluate the inner slicing and then it will evaluate the outer slicing. So it will first evaluate name[0:3] which will give us "Har" and then it will evaluate name["Har"] which will give us "Har" because "Har" is a substring of "Harry". So the final output will be "Har".

print(name[-4:-1]) # output : arr , because it will start from index -4 and end at index -1 ( not included) and it will give us the substring "arr" from the string "Harry". So the final output will be "arr".

print(name[:4]) # output : Harr , because it will start from index 0 and end at index 4 ( not included) and it will give us the substring "Harr" from the string "Harry". So the final output will be "Harr".

print(name[1:]) # output : arr , because it will start from index 1 and end at index 4 ( not included) and it will give us the substring "arr" from the string "Harry". So the final output will be "arr".

Word = "amazing" 
Word = Word[:7]  # word [0:7] – 'amazing' 
Word = Word[0:]  # word [0:7] – 'amazing'