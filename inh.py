class vehicle:
	def drive(self):
		print("Drive Vehicle")

class car(vehicle):
	def cdrive(self):
		vehicle.drive(self)
		print("car")



p1=car()
p1.cdrive()
p1.drive()