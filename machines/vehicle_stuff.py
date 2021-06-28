class Vehicle:

	# the color should not be changed outside of the class specification.
	# this is a class attribute
	vehicle_counter = 0
	
	def __init__(self, body_type, make): # <- !!important!!
		# specify the attributes of the vehicle here
		self.vehicle_body = body_type # must use self to be able to use it on objects like car1 and car2
		self.vehicle_make = make
		Vehicle.vehicle_counter += 1

	def get_vehicle_count(self):
		return Vehicle.vehicle_counter

	def drive(self):
		print("vehicle driving...")

class Truck(Vehicle): # put Vehicle in () to inherit the Vehicle Class
    
    def drive(self):
        print("Truck driving...")

class Motorcycle(Vehicle): # put Vehicle in () to inherit the Vehicle Class
    
    def drive(self):
        print("Motorcycling driving very fast...")