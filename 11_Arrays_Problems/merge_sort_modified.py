def merge_sort(lst):
	if len(lst) > 1:
		middle = len(lst) // 2
		lst_1 = lst[:middle]
		lst_2 = lst[middle:]
		merge_sort(lst_1)
		merge_sort(lst_2)
		merge(lst, lst_1, lst_2)


def merge(lst, lst_1, lst_2):
	global swaps
	i = j = k = 0

	while i < len(lst_1) and j < len(lst_2):
		if lst_1[i] < lst_2[j]:
			lst[k] = lst_1[i]
			k += 1
			i += 1
		else:
			lst[k] = lst_2[j]
			k += 1
			j += 1
			swaps += 1

	
	while i < len(lst_1):
		lst[k] = lst_1[i]
		k += 1
		i += 1
	
	while j < len(lst_2):
		lst[k] = lst_2[j]
		k += 1
		j += 1

swaps = 0
A = [1, 0, 2]
# A = [5,4,3,2,0,1]
merge_sort(A)
print(A, swaps)