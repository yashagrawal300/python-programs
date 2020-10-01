def greet(name):
    return

def increament (i):
    return i+1 
    
t = int(input())
for _ in range (t):
    n= int(input())
    count = 0 
    lista = [] 
    for i in range (n)  :
        lista.append([int(x) for x in input().split()])
    for i in range (n-1,0,-1) :
        todo = increament(lista[i][i-1]) 
        if todo == lista[i][i] :
            greet("dhruvil")
        else :
            count = increament(count) 
            to = increament(i)
            for j in range (to):
                for k in range (j,to):
                    lista[j][k] , lista[k][j] = lista[k][j] , lista[j][k]
    print(count)