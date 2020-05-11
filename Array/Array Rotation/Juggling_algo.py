# Consider GCD or HCF of n,d, 
n =12
d= 3
arr =[]
for i in range(n):
    arr.append(i+1)
# print(arr)

def gcd(a,b):
    if b ==0:
        return a
    else:
        return gcd(b,a%b)

def left_rotation(arr,n=12,d=3):
    d = d%n
    g_c_d = gcd(d,n)

    for i in range(g_c_d):
        temp = arr[i]
        j =i
        while True: 
            k = j+d
            if k>=n:
                k = k-n
            if k ==i:
                break
            arr[j] =arr[k]

            j=k
            arr[j] = temp
    return arr

print(left_rotation(arr)) 

