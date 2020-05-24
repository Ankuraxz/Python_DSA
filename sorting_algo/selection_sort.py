#selection sort
#this is algo for soring by selection.
#it scan slices from l[0:len(l)],l[1:len(l)]........
def selection_sort(l):
  for start in range(len(l)):
    minpos=start
    for i in range(start,len(l)):
      if l[i]<l[minpos]:
        minpos=i
        (l[start],l[minpos])=(l[minpos],l[start])
  return(l)
a=[5,4,3,2,1,11,2,23,45,56]
selection_sort(a)

#time complexity for algo is O(n^2) where n is the number of elements in list.
