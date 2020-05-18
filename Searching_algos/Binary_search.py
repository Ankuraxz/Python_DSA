arr = [1,3,5,12,654,76,2,67,32,4]
arr.sort()
print(arr)
# Works only on sorted array

maxm = len(arr)-1
minm = 0
mid = (maxm+minm)//2 # middle is integer
n = 67
while True:
    if n >arr[mid]:
        minm = mid+1
        mid = (maxm+minm)//2
    
    elif n <arr[mid]:
        maxm = mid-1
        mid = (maxm+minm)//2
    elif n == arr[mid]:
        print("no.",n,"found at location", mid+1)
        break




