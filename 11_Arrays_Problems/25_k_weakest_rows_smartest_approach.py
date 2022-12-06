def kWeakestRows(mat, k):
    # binary serach
    def binary_search(row):
        lower_bound = 0
        upper_bound = len(row)-1

        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2

            if row[mid] == 1:
                lower_bound = mid+1
            else:
                upper_bound = mid-1

        if row[mid] == 0:
            return mid
        else:
            return mid+1
            

    rows    = len(mat) 
    columns = len(mat[0])

    soldiers_count = [[binary_search(mat[i]), i] for i in range(rows)]

    soldiers_count.sort()

    return [soldiers_count[i][1] for i in range(k)]






# mat = [
#         [1,1,0,0,0],
#         [1,1,1,1,0],
#         [1,0,0,0,0],
#         [1,1,0,0,0],
#         [1,1,1,1,1]
#       ]
# k = 3


mat = [
        [1,0,0,0],
        [1,1,1,1],
        [1,0,0,0],
        [1,0,0,0]
      ] 
k = 2


# mat = [
#         [1,0],
#         [0,0],
#         [1,0]
#       ]
# k = 2

print(kWeakestRows(mat, k))