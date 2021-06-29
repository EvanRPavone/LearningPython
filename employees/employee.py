class Employee:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self): # string dunder method
		return self.name + " age is " + str(self.age)

	def __len__(self):
		return self.age
