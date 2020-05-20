#right rotation of array
#it avoids unnecessary no. of recursions for large no. of rotations.
a=[1,2,3,4,5]
def right_rot(arr,r): # r is the no. of times to rotate
  if r<len(arr):
    s=r
  else:
    s=r%len(arr)
    #print(s)
  for a in range(s): 
    store=arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
      arr[i+1]=arr[i]
    arr[0]=store
  return(arr)
right_rot(a,27)
