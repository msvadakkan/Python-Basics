class point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def __str__(self):
		return "({0},{1})".format(self.x,self.y)
	def __add__(self,othr):
		x=self.x+othr.x
		y=self.y+othr.y
		return point(x,y)

p1=point(2,3)
p2=point(4,5)
print(p1+p2)