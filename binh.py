n=int(input())
a = []
for c in range(n):
    g=(input())
    a.append(g)

for i in a:
	test = []
	d=int(i)
	i=("{:032b}".format(d))
	j=str(i)
	for p in j:
		if p is '1':
			test.append('0')
		elif p is '0':
			test.append('1')
		else:
			test.append(i)
	print (int(''.join(test),2))
