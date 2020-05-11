n = 7 # no of elements
d = 2 # no of rotation elements
arr = [1,2,3,4,5,6,7] #LIST, NOt ACTUAL ARRAY

def left_rotation(arr, d=2, n=7):
    for _ in range(d):
        leftrot_byone(arr,n)
    return arr

def leftrot_byone(arr,n):
    temp = arr[0]
    for i in range (n-1):
        arr[i] =arr[i+1]
    arr[n-1] = temp

print(left_rotation(arr))