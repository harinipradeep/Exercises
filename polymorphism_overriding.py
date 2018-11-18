class Parent:
	def __init__(self):
		self.value = 5
	def get_value(self):
		return self.value

class Child(Parent):
	def get_value(self):
		return self.value+1

p = Parent()
print(p.get_value())

c = Child()
print(c.get_value())

#$ python polymorphism_overriding.py 
#5
#6
