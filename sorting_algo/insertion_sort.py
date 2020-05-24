#insertion sort
#insert the values on comparing with previous one
# l is any sequence you want to sort in form of list.
def insertion_sort(l): 
  for slice_end in range(len(l)):
    pos=slice_end
    while pos>0 and l[pos]<l[pos-1]:
      (l[pos],l[pos-1])=(l[pos-1],l[pos])
      pos=pos-1                      #it makes the sequence shorter
  return(l)
a=[5,4,3,2,1]
insertion_sort(a)

#time compexity for this algo is O(n^2) where n is the no. of elements in array.
# worst case for this algo is  descending arragned elements.
#if list is alredy sorted it takes no time.
