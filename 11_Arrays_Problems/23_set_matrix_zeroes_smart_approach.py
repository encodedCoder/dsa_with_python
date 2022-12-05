def setZeroes(matrix):
    row_flag    = False
    column_flag = False

    rows    = len(matrix)
    columns = len(matrix[0])

    for i in range(columns):
        if matrix[0][i] == 0:
            row_flag = True
            break

    for i in range(rows):
        if matrix[i][0] == 0:
            column_flag = True
            break

    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] == 0:
                matrix[0][j] = matrix[i][0] = 0

    for i in range(1, rows):
        for j in range(1, columns):
            if 0 in [matrix[0][j], matrix[i][0]]:
                matrix[i][j] = 0

    if row_flag:
        for i in range(columns):
            matrix[0][i] = 0

    if column_flag:
        for i in range(rows):
            matrix[i][0] = 0



matrix = [[1,1,1],[1,0,1],[1,1,1]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix = [[0,1,1,0],[1,1,0,1],[1,1,1,1]]
setZeroes(matrix)
print(matrix)