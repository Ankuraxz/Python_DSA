#target=A-->Z
#ascii range for this is 65-90
s=set(input("enter the string")) #taking sting as a set will remove all the duplicacy of letters and other characters.
c=0 #here we shall count the number of target letters
for i in s:
    i=i.capitalize() # so that we can decide a ascii range
    if 64<ord(i)<91: #condition to check the ascii range
        c=c+1
if c==26:
    print('pangram')
else:
    print('not pangram')
