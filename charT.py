
s=input("Enter String \n")

d=list(s.split(' '))
c=0

#charCount
print("char:",len(s))

#wordsCount
for i in range(len(d)):
	if(d[i]!=''):
		c=c+1
print("words:",c)
f=[]
ff=0
#searching
sr=input("Enter a word to search")
for i in range(len(d)):
	if(d[i]==sr):
		ff=f+1


