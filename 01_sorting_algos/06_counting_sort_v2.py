def counting_sort(A):
	max_ele = max(A)
	C = [0]*(max_ele+1)

	#count the elements occurrences
	for i in range(len(A)):
		C[A[i]] += 1

	#find the cummulative sum
	for i in range(1, len(C)):
		C[i] += C[i-1]

	#apply the counting sort logic for stable sorting
	B = [0]*len(A)
	for i in range(len(A)-1, -1, -1):
		B[C[A[i]]-1] = A[i]
		C[A[i]] -= 1
	
	for i in range(len(B)):
		A[i] = B[i]
    



A = [1, 8, 4, 2, 3, 1, 6, 8, 4, 5, 2, 2, 6]
print(A)
counting_sort(A)
print(A)