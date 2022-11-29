def binary_search_recursive(lst, num):
	if len(lst) == 1:
		if lst[0] == num:
			return True
		else:
			return False

	lst_half = len(lst)//2
	if lst[lst_half] == num:
		return True
	elif num > lst[lst_half]:
		return binary_search_recursive(lst[lst_half:], num)
	elif num < lst[lst_half]:
		return binary_search_recursive(lst[:lst_half], num)



def binary_search_iterative(lst, num, lower_bound, upper_bound):
	while lower_bound <= upper_bound:
		middle_index = (lower_bound + upper_bound) // 2
		if lst[middle_index] == num:
			return middle_index
		elif lst[middle_index] > num:
			upper_bound = middle_index - 1
		elif lst[middle_index] < num:
			lower_bound = middle_index + 1
	return False



lst = [2, 8, 9, 11, 12, 13, 14, 15, 20, 21, 25, 26, 28]

num = 9
print("Index of '{}' in list is '{}'".format(num, binary_search_iterative(lst, num, 0, len(lst)-1)))