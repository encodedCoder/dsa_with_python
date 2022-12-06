def kWeakestRows(mat, k):
    rows    = len(mat) 
    columns = len(mat[0])

    soldiers_count = []
    for i in range(rows):
        for j in range(columns-1, -1, -1):
            if mat[i][j] == 1:
                soldiers_count.append([j+1, i])
                break
            elif mat[i][j] == 0 and j == 0:
                soldiers_count.append([0, i])
                break

    soldiers_count.sort()

    weakest_rows = []
    for i in range(k):
        weakest_rows.append(soldiers_count[i][1])

    return weakest_rows




mat = [
        [1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]
      ]
k = 3


mat = [
        [1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]
      ] 
k = 2


mat = [
        [1,0],
        [0,0],
        [1,0]
      ]
k = 2

print(kWeakestRows(mat, k))

