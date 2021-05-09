def onemaker(n,count=0):
    if n==1:
        return count
    elif n%2==0 and n>1: #even
        #print("even")
        n = n//2
        return onemaker(n,count+1)
    elif n%2 !=0 and n>1: #odd
        #print("odd")
        n = n+1
        return onemaker(n,count+1)
    else:
        return("Provide Right output")




n = input("Binary Number here ") #binary number
n = int(n,2) #Binary to Decimal
#print(n)
counter = onemaker(n)
print(counter)
