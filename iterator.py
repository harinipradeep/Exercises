x = [1,2,3,4]
y = iter(x)
z = iter(x)
for i in y:
	print(i)
print(next(z))
print(next(z))
print(next(y))
#Generator gnerates the value on demand.
#y is the generator object and we have already iterated over all the
#generated values. Since there is no more values in the generator to
#iterate..this throws an error.


#$ python iterator.py 
#1
#2
#3
#4
#1
#2
#Traceback (most recent call last):
#  File "iterator.py", line 8, in <module>
#    print(next(y))
#StopIteration



