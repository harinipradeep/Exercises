#Mammal class is derived from Animal class and Tiger class is derived from Mammal class. 
#This is an example of Multilevel inheritance.
#Dog class is derived from NonMarineAnimal and NonWingedAnimal class.
#Since more than one parent class is there. This is an example of Multiple inheritance.


class Animal(object):
	def __init__(self, animal_name):
		print(animal_name, 'is an animal')

class Mammal(Animal):
	def __init__(self, mammal_name):
		print(mammal_name, 'is a warm blooded animal.')
		super(Mammal, self).__init__(mammal_name)

class Tiger(Mammal):
	def __init__(self):
		print('Tiger is a wild animal')
		super(Tiger, self).__init__('Tiger')

class NonMarineAnimal(Mammal):
	def __init__(self, non_marine_mammal_name):
		print(non_marine_mammal_name, "can't swim.")
		super(NonMarineAnimal, self).__init__(non_marine_mammal_name)

class NonWingedAnimal(Mammal):
	def __init__(self, non_winged_animal_name):
		print(non_winged_animal_name, "can't fly.")
		super(NonWingedAnimal, self).__init__(non_winged_animal_name)


class Dog(NonMarineAnimal, NonWingedAnimal):
	def __init__(self):
		print('Dog is a pet animal')
		super(Dog, self).__init__('Dog')

d1 = Dog()
t1 = Tiger()
#Method resolution order is the order in which the method should be inherited in
#presence of multiple inheritance
print(Dog.__mro__)
print(Tiger.__mro__)


#$ python super_example.py 
#Dog is a pet animal
#('Dog', "can't swim.")
#('Dog', "can't fly.")
#('Dog', 'is a warm blooded animal.')
#('Dog', 'is an animal')
#Tiger is a wild animal
#('Tiger', 'is a warm blooded animal.')
#('Tiger', 'is an animal')
#(<class '__main__.Dog'>, <class '__main__.NonMarineAnimal'>, <class '__main__.NonWingedAnimal'>, <class '__main__.Mammal'>, <class '__main__.Animal'>, <type 'object'>)
#(<class '__main__.Tiger'>, <class '__main__.Mammal'>, <class '__main__.Animal'>, <type 'object'>)

