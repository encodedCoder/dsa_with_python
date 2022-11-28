def selection_sort(lst):
	i = 0
	while i < len(lst):
		min_index = i
		j = i + 1
		while j < len(lst):
			if lst[min_index] > lst[j]:
				min_index = j
			j += 1
		if min_index != i:
			lst[min_index], lst[i] = lst[i], lst[min_index]
		i += 1

lst = [4, 2, 3, 6, 8, 17, 5, 9]
print(lst)
selection_sort(lst)
print(lst)