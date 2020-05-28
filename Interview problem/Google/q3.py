s = input("Enter string")
d = {}
for i in range(len(s)):
    # print(s[i])
    if s[i] in d.keys(): # as soon as 1st char repeated
        d[s[i]] = 1
        print(s[i]) #repetead char
        print(i) #index
        break
    else:
        d[s[i]] = 1

# print(d) # key:- Unique Keys, value:- count of char
# print(d.keys())
