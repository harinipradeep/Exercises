def binarysearch(lst, item):
	first = 0
	last = len(lst)-1
	found = False
	while first<=last and not found:
		mid = (first+last)/2
		if lst[mid] == item:
			found = True
		else:
			if lst[mid]<item:
				first = mid + 1
			else:
				last = mid-1
	return found

lst = [32,12,35,9,13,8,16]
lst.sort()
print(binarysearch(lst,16))
print(binarysearch(lst,3))

#$ python binarysearch.py 
#True
#False
