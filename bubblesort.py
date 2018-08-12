def bubblesort(lst):
	for num in range(len(lst)-1,0,-1):
		for i in range(num):
			if lst[i] >= lst[i+1]:
				tmp = lst[i]
				lst[i] = lst[i+1]
				lst[i+1] = tmp

lst = [34,12,67,9,23]
bubblesort(lst)
print(lst)

#$ python bubblesort.py 
#[9, 12, 23, 34, 67]
