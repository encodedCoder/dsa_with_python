def separate_0s_and_1s(arr):
	i = 0
	j = len(arr)-1
	while i < j:
		if arr[i] == 0:
			i += 1
		if arr[j] == 1:
			j -= 1
		else:
			arr[i], arr[j] = arr[j], arr[i]


arr = [1, 0, 0, 1, 0, 1, 1, 0, 1]
separate_0s_and_1s(arr)
print(arr)