for i in range(int(input())):
	n,x=list(map(int,input().split()))
	l=list(map(int,input().split()))
	l.sort(reverse=True)
	c=0
	a=0
	for j in l:
		c+=1
		a+=j
		if a>=x:
			print(c)
			break
	else:
		print(-1)