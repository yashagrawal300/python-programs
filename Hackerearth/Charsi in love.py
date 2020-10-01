import math
def love(n,arr):
    l = 0
    h = len(arr)-1
    while l<=h:
        if arr[l]+arr[h]>n:
            h-=1
        elif arr[l]+arr[h]<n:
            l+=1
        else:
            return "YES"
    
    return "NO"



n = int(input())
n = n*2
arr = []
for i in range(1,int(math.sqrt(n))):
    arr.append(i*(i+1))

print(love(n,arr))
