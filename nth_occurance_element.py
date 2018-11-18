data = ['a','b','c','a','b','a','a','b','a','c']
element = raw_input("Enter the element")
occ = int(raw_input("Enter the number of occurance"))
count = 0
i = 0
if element not in data:
	print("Element is not in the list. Please provide valid input")
else:
	while(i<len(data)):
		if data[i] == element:
			count = count+1
			if count==occ:
				print("Index of nth occurance of "+data[i]+" :"+str(i))
				break
			i = i + 1
		else:
			i = i + 1