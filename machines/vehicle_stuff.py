class Car:

	# the color should not be changed outside of the class specification.
	# this is a class attribute
	color = 'red'
	vehicle_counter = 0
	
	def __init__(self, body_type, make): # <- !!important!!
		# specify the attributes of the vehicle here
		self.vehicle_body = body_type # must use self to be able to use it on objects like car1 and car2
		self.vehicle_make = make
		Car.vehicle_counter += 1

	def get_vehicle_count(self):
		return Car.vehicle_counter

