n = str(input("number :-  "))
sum=0
for i in n:
    
    sum+=int(i)*int(i)*int(i)
    
if sum == int(n):
    print("Armstrong")
else:
    print("Not Armstrong")
