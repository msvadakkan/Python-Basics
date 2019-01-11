class std:
	Rno=0
	name=""
	crse=""
	def __init__(self,rn,nm,crs):
		self.iRno=rn
		self.iname=nm
		self.icrse=crs
	def adds(self):
		std.Rno=self.iRno
		std.name=self.iname
		std.crse=self.icrse
	def display(self):
		print("\nRoll No.   :",std.Rno)
		print("Roll name  :",std.name)
		print("Roll coures:",std.crse)	
		
s=std(1,"safvan","cse")
s1=std(2,"Merin","ECE")
s2=std(3,"Minu","ECE")
s3=std(4,"Ani","MCA")
s.adds()
s.display()
s1.adds()
s1.display()
s2.adds()
s2.display()
s3.adds()
s3.display()
