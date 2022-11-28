def bubble_sort(lst):
	for i in range(len(lst)-1, 0, -1):
		for j in range(i):
			if lst[j] > lst[j+1]:
				temp = lst[j]
				lst[j] = lst[j+1]
				lst[j+1] = temp

lst = [20, 69, 8, 21, 36, 57, 12, 42]
bubble_sort(lst)
print(lst)