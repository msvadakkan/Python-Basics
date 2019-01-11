n,t=input().split()
n=int(n)
t=int(t)

if(n>2):
	n+=1
	ary=list(range(1,n))
	cd=[(x-y) for x in ary for y in ary]
	c=int(cd.count(1))
		c=c-1
	print(c)
else:
	print("Error: Minimum 2 numbers required")