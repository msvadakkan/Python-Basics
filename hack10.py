import math
n=int(input())
a=[]
b=[]
for i in range(n):
	a.append(input())
b=bnT()
print(b)
# for l in a:
# 	print(b[int(a[l])])

def bnT(x):
	b=[]
	for r in range(120):
		n=r
		l=list(str(n))
		a=l[::-1]
		x=0
		f=0
		for i in a:
			d=(int(i)*math.pow(2,x))
			f=int(d+f)
			x=x+1

		b.append(f:r)
	return(sorted(b))




