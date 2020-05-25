# Taking the inputs
arr = list(map(int,input(" Enter space seperated integer").rstrip().split()))
x = int(input("Enter the number"))

# Selecting only those elements which are less than equal to X, as only positive integer are allowed --> Optimization1
subarr=[]
for i in arr:
    if i <= x: # Cause only +ve no present
        subarr.append(i)
# print(subarr)


def interpolationSearch(arr, n, x):  # Interpolation Search, read more about it here:- https://www.geeksforgeeks.org/interpolation-search/
    # Find indexs of two corners 
    lo = 0
    hi = (n - 1) 
   
    # Since array is sorted, an element present 
    # in array must be in range defined by corner 
    while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == x:  
                return lo 
            return -1 
          
        # Probing the position with keeping 
        # uniform distribution in mind. 
        pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 
  
        # Condition of target found 
        if arr[pos] == x: 
            return pos 
   
        # If x is larger, x is in upper part 
        if arr[pos] < x: 
            lo = pos + 1 
   
        # If x is smaller, x is in lower part 
        else: 
            hi = pos - 1 
      
    return -1

# Checking is x-arr[i] is present or not, as x-arr[i] +arr[i] = x

result =0
subarr.sort()
l = len(subarr)
for i in range(l):
    subarrx = subarr[i:] # -->optimization2
    n = len(subarrx)
    index = interpolationSearch(subarrx,n,(x-subarr[i])) # --> Optimization 3
    if index != -1 :
        result +=1
        break

if result >0:
    print("yes")
else:
    print("no")   

