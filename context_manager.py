
#Context manager helps to manage the resources. It will allocate and release 
#the resources when we want to..Most used context manager is with keyword

with open("/tmp/test") as f:
	print(f.read())
	print(f.closed)

file = open("/tmp/test")
print(file.closed) 
file.close()
print(file.closed)

#when we come out of the indented block the file is automatically closed.
#where as when we do not use with we have to explicitly close the file.

#$ python context_manager.py 
#hellloooo

#False
#False
#True
