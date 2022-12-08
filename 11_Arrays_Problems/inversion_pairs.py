def inversion_pairs(lst):
	length_of_lst = len(lst)
	for i in range(length_of_lst):
		j = i+1
		while j < length_of_lst:
			if lst[i] > lst[j]:
				print("({}, {})".format(lst[i], lst[j]), end = ', ')
			j += 1
		print("")


lst = [4, 3, 1, 2, 5]
lst = [2, 3, 4, 5, 1]
inversion_pairs(lst)