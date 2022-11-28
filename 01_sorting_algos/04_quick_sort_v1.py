def quick_sort(lst, p, r):
	if p < r:
		q = partition(lst, p, r)
		quick_sort(lst, p, q-1)
		quick_sort(lst, q+1, r)

def partition(lst, p, r):
	pivot  = lst[r]
	i = p-1
	j = p
	while j < r:
		if pivot > lst[j]:
			i += 1
			lst[i], lst[j] = lst[j], lst[i]
		j += 1
	i += 1
	lst[r], lst[i] = lst[i], lst[r]
	return i 



lst = [20, 69, 8, 21, 36, 57, 12, 42]
print("Unsorted list:", lst)
quick_sort(lst, 0, len(lst)-1)
print("Sorted list:  ",  lst)