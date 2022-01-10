for i in range(int(input())):
	a,b,c=list(map(int,input().split()))


	f = (a+c)/2 
	e = 2*b-c
	g = 2*b-a

	if f%b==0 and f>0:
		print("yes")
	elif e%a==0 and e>0:
		print("yes")
	elif g%c==0 and g>0:
		print("yes")
	else:
		print("no")


