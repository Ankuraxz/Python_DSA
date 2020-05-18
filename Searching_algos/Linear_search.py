arr = [1,3,5,12,654,76,2,67,32,4]
 # worst case to be found =4
n=4
 for i in range (len(arr)):
     if arr[i]==n:
         print("no. found at location",i+1)
         break
