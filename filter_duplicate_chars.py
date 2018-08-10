
import sys
word = sys.stdin.read()
unique_chars = set()
map(unique_chars.add, word)
print("Filtered duplicate characters:")
print(unique_chars)

#$ python filter_duplicate_chars.py 
#harini
#Filtered duplicate characters:
#set(['a', 'i', 'h', '\n', 'n', 'r'])