"""


Given an array A of size N and an integer K , check if there exist any pair of index i,j such that Ai+Aj=K and i≠j


"""


def main():
    for _ in range(int(input())):
        n,k = map(int,input().split())
        a = list(map(int,input().split()))
        a.sort()
        i = 0
        j = n-1
        flag = 0
        while i<j:
            if a[i]+a[j]==k:
                print('Yes')
                flag = 1
                break
            elif (a[i]+a[j])>k:
                j-=1
            else:
                i+=1
        if not(flag):
            print('No')
            
if __name__=="__main__":
    main()
