def merge_sort(lst):
	if len(lst) > 1:
		mid = len(lst)// 2
		left = lst[:mid]
		right = lst[mid:]
		merge_sort(left)
		merge_sort(right)
		merge(lst, left, right)

def merge(lst, left, right):
	i = 0; j = 0; k = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			lst[k] = left[i]
			i += 1
		else:
			lst[k] = right[j]
			j += 1
		k += 1

	while i < len(left):
		lst[k] = left[i]
		i += 1; k += 1

	while j < len(right):
		lst[k] = right[j]
		j += 1; k += 1

lst = [4, 6, 8, 9, 3, 7, 10, 5, 2]
merge_sort(lst)
print(lst)