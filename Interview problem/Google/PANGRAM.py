
# 65-90: A-->Z #TARGET
#97-122 : a-->z
# Logic :- input each chracter of string as a ascii value, it is always easy to work with numbers

a = input("Enter string")

# a_ will hold ascii value of all capitalised chracters

a_ = []
for i in a:
    i = i.capitalize() # captializing all chars
    a_.append(ord(i))
# print(a_)

s = set(a_) # attaining unique chars
# print(s)
# s has ASCII code of all unique chars of input string
# removing all symbols and saving capitalised letter in chars
chars =[]
for i in s:
    if i <= 90 and i >= 65: #range (65-90)
        chars.append(i)

# print(chars)
# print(len(chars))
# Now using len ( a list from 65-90 ascii is 26 (26 a-->z))

if len(chars) == 26:
    print("pangram")
else:
    print("not pangram") 
