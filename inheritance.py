class Animal(object):
	def __init__(self):
		self.legs = "4"

	def walk(self):
		print("Animal walks with "+ self.legs +" legs")

class Dog(Animal):
	def __init__(self, value):
		self.value = value
		super(Dog, self).__init__()

	def bark(self):
		print("Dog is an animal which "+ self.value)

	def do_both(self):
		self.walk()
		self.bark()


parent = Animal()
parent.walk()

child = Dog("Barks")
child.bark()
child.do_both()


#$ python inheritance.py 
#Animal walks with 4 legs
#Dog is an animal which Barks
#Animal walks with 4 legs
#Dog is an animal which Barks




