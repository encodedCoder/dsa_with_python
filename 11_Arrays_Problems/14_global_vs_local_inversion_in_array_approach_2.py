def isIdealPermutation(A):
	n = len(A)
	if n <= 2:
		return True

	max_ = 0	
	for i in range(len(A)-2):
		max_ = max(max_, A[i])
		if max_ > A[i+2]:
			return False
	else:
		return True



# A = [1, 0, 2]
# A = [1, 2, 0]
# A = [0, 2, 1]
# A = [1, 0]
# A = [2, 1, 0]
# A = [1,0]
# A = [0, 1, 2]
# A = [1,5,2,6,3,0]
# A = [4, 6, 1, 7, 3, 2, 5]
# A = [7, 5, 1, 3, 4, 6]
print(isIdealPermutation(A))