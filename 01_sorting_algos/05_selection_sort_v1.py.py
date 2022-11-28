def selection_sort(lst):
	for i in range(len(lst)-1, 0, -1):
		max = 0
		for j in range(1, i+1):
			if lst[max] < lst[j]:
				max = j
		lst[max], lst[i] = lst[i], lst[max] 

lst = [56, 69, 87, 21, 36, 57, 12, 42]
selection_sort(lst)
print(lst)