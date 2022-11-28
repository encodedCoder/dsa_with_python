# Something wrong with the code (may be)
# -------Warning---------------
# Find out what can cause inconsistent in the code
# Checkout the end comments for solution

def insertion_sort(lst):
	for i in range(1, len(lst)):
		j = i-1
		key = lst[i]
		for j in range(j, -2, -1):
			if key < lst[j]:
				lst[j+1] = lst[j]
			elif key > lst[j]:
				break
		lst[j+1] = key

lst = [6, 12, 5, 2, 4, 3, 8, 20, 9]
insertion_sort(lst)
print(lst)




# Solution:-
# "for j in range(j, -2, -1)" here loop is going to acccess the (continued to next line)
# "-1" index element of list the list which can cause the inconsistency in the code