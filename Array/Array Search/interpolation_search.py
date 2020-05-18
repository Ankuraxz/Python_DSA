arr = [1,3,5,12,654,76,2,67,32,4]
arr.sort()
print(arr)
# Works only on sorted array
x  = 67

hi = len(arr)-1
lo = 0
# range_ = hi-lo
# pos = int(lo + ((x-arr[lo])*(range_))/(arr[hi]-arr[lo]))
pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 

while True:
    if x >arr[int(pos)]:
        lo = pos+1
        arr = arr[pos:]
        hi = len(arr)-1
        # range_ = hi-lo
        # pos = int(lo + ((x-arr[lo])*(range_))/(arr[hi]-arr[lo]))
        pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 
            
    elif x <arr[int(pos)]:
        arr = arr[:pos]
        hi = len(arr)-1
        # range_ = hi-lo
        # pos = int(lo + ((x-arr[lo])*(range_))/(arr[hi]-arr[lo]))
        pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 

    elif x == arr[int(pos)]:
        print("no.",x,"found at location", int(pos+1))
        break