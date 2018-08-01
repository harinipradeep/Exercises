#Mammal class is derived from Animal class.
#Dog and Tiger class are derived from Mammal class. This is an 
#example of Multiple inheritance


class Animal(object):
	def __init__(self, animal_name):
		print(animal_name, 'is an animal')

class Mammal(Animal):
	def __init__(self, mammal_name):
		print(mammal_name, 'is a warm blooded animal.')
		super(Mammal, self).__init__(mammal_name)

class Dog(Mammal):
	def __init__(self):
		print('Dog is a pet animal')
		super(Dog, self).__init__('Dog')

class Tiger(Mammal):
	def __init__(self):
		print('Tiger is a wild animal')
		super(Tiger, self).__init__('Tiger')

d1 = Dog()
t1 = Tiger()


#$ python super_example.py 
#Dog is a pet animal
#('Dog', 'is a warm blooded animal.')
#('Dog', 'is an animal')
#Tiger is a wild animal
#('Tiger', 'is a warm blooded animal.')
#('Tiger', 'is an animal')
