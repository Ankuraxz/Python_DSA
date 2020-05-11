n = 7 # no of elements
d = 2 # no of rotation elements
arr = [1,2,3,4,5,6,7] #LIST, NOt ACTUAL ARRAY
temp = arr[:d] #store first d elements in temp

# print (temp)

for i in range (n-d):
    arr[i] = arr[i+d]
    print(arr[i])

arr[-d:] = temp
# print(arr[-d:])
print(arr)