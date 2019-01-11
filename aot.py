class std:
	ar=0
	def __init__(self,br,ht):
		self.h=ht
		self.b=br

	def adds(self):
		std.ar=(self.h*self.b)*.5
		
	def display(self):
		print("\nResult   :",std.ar)
			
		
s=std(5,3)
s.adds()
s.display()
