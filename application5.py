# SECTION 5

# 1. Revisiting the Differences between Methods and Functions

mylist = [1,2,3,4]

mylist.pop() # <- Method

print(mylist)

# -> [1,2,3]

mylist = [1,2,3]

max_number = max([1,2,3,4,100,900]) # <- Function

# mylist.max() -> this isn't a thing because max is a function
# error -> unresolved attribute reference 'max' for class 'list

print(max_number) # -> 900

def myname(name):
	print("Hello " + name)

myname("Evan")

# 2. Classes and Objects

class Vehicle:
	def __init__(self, body_type, make): # <- !!important!!
		# specify the attributes of the vehicle here
		self.vehicle_body = body_type # must use self to be able to use it on objects like car1 and car2
		self.vehicle_make = make

car1 = Vehicle('Sedan', 'Toyota') # -> This is how you would initialize a vehicle
print(car1.vehicle_body)
print(car1.vehicle_make)

car2 = Vehicle('SUV', 'Subaru')
print(car2.vehicle_body)
print(car2.vehicle_make)

print(type(car1))
# -> <class '__main__.Vehicle'>