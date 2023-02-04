n = int(input("Number :-  "))
res=1
if n ==0 or n== 1:
    print(1)

else:
    while n>1:
        res*=n
        n-=1
    print(res)
