#Vowel Generator
def vowels():
	yield "a"
	yield "e"
	yield "i"
	yield "o"
	yield "u"

for i in vowels():
	print(i)


#$ python generator_method.py 
#a
#e
#i
#o
#u
