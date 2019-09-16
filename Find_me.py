#Three integers are given in the input- N, A, B. Find an integer C such that N = A + B + C.

x = input()
x = x.split(' ')
n = int(x[0])
a = int(x[1])
b = int(x[2])
print(n-a-b)
