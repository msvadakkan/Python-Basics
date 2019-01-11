import math
b=[]
for r in range(120):
	n=r
	l=list(str(n))
	a=l[::-1]
	x=0
	f=0
	for i in a:
		d=(int(i)*math.pow(2,x))
		f=d+f
		x=x+1
	b.append((f,i))
print(sorted(b))
