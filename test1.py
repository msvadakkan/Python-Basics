#a=input("value")
a="saf100 mer50 ani25"
#print(ord(a))
t1=list(a.split())
#print(t1)

t3=[]
for i in range(len(t1)):
		c=list(t1[i])
		#print(c)
		for j in c:
			if j.isdigit():
				t3.append(j)
		a="".join(str(t3))
		print(a)
