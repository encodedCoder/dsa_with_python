def setZeroes(matrix):
    rows    = len(matrix)
    columns = len(matrix[0]) 
    # print(rows, columns)
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                for k in range(columns):
                    if matrix[i][k] != 0:
                        matrix[i][k] = 'A'
                for k in range(rows):
                    if matrix[k][j] != 0:
                        matrix[k][j] = 'A'

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == None:
                matrix[i][j] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[0,1,1,0],[1,1,0,1],[1,1,1,1]]
setZeroes(matrix)
print(matrix)