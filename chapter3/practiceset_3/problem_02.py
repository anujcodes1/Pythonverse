letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|>'''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "20/10/2020")) # output : Dear Harry, You are selected! 20/10/2020 , because it will first replace the substring "<|Name|>" with "Harry" and then it will replace the substring "<|Date|>" with "20/10/2020". So the final output will be "Dear Harry, You are selected! 20/10/2020".


