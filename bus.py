
def bus_avail(bus,ppl,seat):
	num = ppl-(bus*seat) 
	if num <= 0:
		print "There are available seats for the given number of people"
	else:
		print "there are less seats available"
num_of_bus = input("Enter the number of buses")
num_of_ppl = input("Enter the number of people")
num_of_seats = input("Enter the number of seats in each buses")
bus_avail(num_of_bus,num_of_ppl,num_of_seats)