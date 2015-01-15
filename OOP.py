class Animal:
	def __init__(self,colour,age,name,size):
		self.name = name
		self.age = age
		self.colour = colour
		self.size = size
dog = Animal("chocolate",22,"brown","huge")
print(dog.name)
print(dog.age)
print(dog.colour)
print(dog.size)

