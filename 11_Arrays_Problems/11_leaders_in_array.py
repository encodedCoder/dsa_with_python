def find_leaders(arr):
	leaders_lst = [0]
	leaders_lst[0] = arr[-1]
	for i in range(len(arr)-2, -1, -1):
		if arr[i] >= leaders_lst[0]:
			leaders_lst.insert(0, arr[i])

	return leaders_lst

arr = [8, 4, 2, 3, 1, 5, 4, 2]
arr = [10, 6, 3, 1, 7, 9]
print(find_leaders(arr))