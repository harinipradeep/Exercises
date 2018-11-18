#$ python context_manager.py 
#helooooooo


#Context manager helps to manage the resources. It will allocate and release 
#the resources when we want to..Most used context manager is with keyword

with open("/tmp/test") as f:
	print(f.read())

#when we come out of the indented block the file is automatically closed.