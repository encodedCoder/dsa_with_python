def is_tableau(tableau):
	# Check if first row is good for young tableau
	for i in range(1, len(tableau[0])):
		if tableau[0][i] < tableau[0][i-1]:
			return False

	# Check if first column is good for yound tableau
	for i in range(1, len(tableau)):
		if tableau[i][0] < tableau[i-1][0]:
			return False

	# Check the rest of array for young tableau success
	for i in range(1, len(tableau)):
		for j in range(1, len(tableau[i])):
			if tableau[i][j] < tableau[i-1][j] or tableau[i][j] < tableau[i][j-1]:
				return False
	return True



tableau_1 = [[1,2,5,14],
			 [3,4,6,23],
			 [10,12,18,25],
			 [31, 9999, 9999, 9999]
			]

print(is_tableau(tableau_1))