def linear_search(lst, num):
	for i in range(len(lst)):
		if lst[i] == num:
			return i
	return False




lst = [18, 56, 87, 32, 61, 94, 21, 56, 41, 47, 38, 0]

num = 0
index = linear_search(lst, num)
if index is not False:
	print("Yes, Element you're looking for is present.\nElement '{}' Found at {}".format(num, index))
