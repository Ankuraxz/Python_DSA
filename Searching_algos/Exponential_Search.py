def Binarysearch(subarr,n):
    
    maxm = len(subarr)-1
    minm = 0
    mid = (maxm+minm)//2 # middle is integer
    while True:
        if n >subarr[mid]:
            
            minm = mid+1
            mid = (maxm+minm)//2
        
        elif n <subarr[mid]:
            
            maxm = mid-1
            mid = (maxm+minm)//2
        elif n == subarr[mid]:
            # print("no.",n,"found at location", mid+1)
            return mid+1
            
def exponential(arr,x):
    arr.sort()
    l = len(arr)
    # print(arr)
    i =0
    subarr=arr[:int(2*i+1)]
    
    while len(subarr) <l:
        # print(subarr)
        
        ref = subarr[-1]
        # print(ref)
        if ref < x:
            
            i+=1
            subarr= arr[:int(2*i)]
            # print(subarr)
        elif ref == x:
            
            loc = 2**i-1
            print("no.",x,"found at location",loc)
            break
        elif ref > x:
            loc = Binarysearch(subarr,x)
            print("no.",x,"found at location",loc)
            break

arr = [2,4,5,8,9,70,500,8000]
x = 70
exponential(arr,x)