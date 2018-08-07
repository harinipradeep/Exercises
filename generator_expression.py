numbers = [1,2,3,4,5]
#a generator expression(note:This is not a tuple comprehension)
lazy_squares = (x*x for x in numbers)
print(type(lazy_squares))
for i in numbers:
	#explicit calling of next
	print(next(lazy_squares))
lazy_sum = (x+x for x in numbers)
print(type(lazy_sum))
#implicit calling of next
for i in lazy_sum:
	print(i)




#$ python generator_expression.py 
#<type 'generator'>
#1
#4
#9
#16
#25
#<type 'generator'>
#2
#4
#6
#8
#10