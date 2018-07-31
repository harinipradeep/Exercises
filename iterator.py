x = [1,2,3,4]
y = iter(x)
z = iter(x)
for i in y:
	print(i)
print(next(z))
print(next(z))


#$ python iterator.py 
#1
#2
#3
#4
#1
#2

