#merge sort
#divide and conquer rule
def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while (i+j)<(m+n): #loop until we reach the length of lists
        if i==m:#if a is empty
            c.append(b[j])
            j+=1
        elif j==n:#if b is empty
            c.append(a[i])
            i+=1
        elif a[i]<=b[j]:
            c.append(a[i])
            i+=1
        elif a[i]>b[j]:
            c.append(b[j])
            j+=1
    return(c)

def merge_sort(l,left,right):
    if right-left<=1:#base case
        return(l[left:right])
    if right-left>1:#recursive call
        mid=(left+right)//2
        L=merge_sort(l,left,mid)
        R=merge_sort(l,mid,right)
        return(merge(L,R))

a=[i for i in range(9,0,-1)]
print(a)
merge_sort(a,0,len(a))


# time complexity for this sorting algo is O(nlogn)
# here we are passing three arguments if you want to take only list
# then
# def merge_sort(l):
#     left=0
#     right=len(l)
#     if right-left<=1:#base case
#         return(l[left:right])
#     if right-left>1:#recursive call
#         mid=(left+right)//2
#         L=merge_sort(l,left,mid)
#         R=merge_sort(l,mid,right)
#         return(merge(L,R))
