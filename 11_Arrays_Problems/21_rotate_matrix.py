def rotate(matrix):
    i = 0
    n = len(matrix)-1

    while i < n:
        j = i
        k = 0
        while j < n:
            copy_1 = matrix[j][i]
            copy_2 = matrix[i][n-k]
            copy_3 = matrix[n-k][n]
            copy_4 = matrix[n][j]

            matrix[i][n-k] = copy_1
            matrix[n-k][n] = copy_2
            matrix[n][j]   = copy_3
            matrix[j][i]   = copy_4

            j += 1
            k += 1
        i += 1
        n -= 1



matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# matrix = [[1]]
# matrix = [[1,2],[3,4]]
rotate(matrix)
print(matrix)