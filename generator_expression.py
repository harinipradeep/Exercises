numbers = [1,2,3,4,5]
#a generator expression(note:This is not a tuple comprehension)
lazy_squares = (x*x for x in numbers)
print(type(lazy_squares))
for i in numbers:
	print(next(lazy_squares))


#$ python generator_expression.py 
#<type 'generator'>
#1
#4
#9
#16
#25
