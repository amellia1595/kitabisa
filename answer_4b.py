from heapq import merge
import itertools 

listA = input("List A :")
listB = input("List B :")

listAsort = sorted(listA)
listBsort = sorted(listB)

for (a,b) in itertools.zip_longest(listAsort,listBsort):
	result = list((a,b))
	print(result)
