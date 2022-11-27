def insertion_sort(lst):
	for i in range(1, len(lst), 1):
		key = lst[i]
		j = i-1
		while lst[j] > key and j >= 0:
			lst[j+1] = lst[j]
			j -= 1
		lst[j+1] = key


lst = [4, 6, 8, 9, 3, 7, 1, 5, 2]
insertion_sort(lst)
print(lst)