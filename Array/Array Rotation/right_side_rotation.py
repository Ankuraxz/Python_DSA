#right rotation of array
#it avoids unnecessary no. of recursions for large no. of rotations.
a=[1,2,3,4,5]
n=5 #n is length of array.
def right_rot(arr,r):# r is the no. of times to rotate
  n=len(arr)
  if r<n:
    s=r
  else:
    s=r%n
    #print(s)
  for a in range(s):
    store=arr[n-1]
    for i in range(n-2,-1,-1):
      arr[i+1]=arr[i]
    arr[0]=store
  return(arr)
right_rot(a,27)
