from pdb import set_trace

def countNegatives(grid):
    rows    = len(grid)
    columns = len(grid[0])

    count = 0
    start_j = 0
    for i in range(rows-1, -1, -1):
        for j in range(start_j, columns):
            if grid[i][j] < 0:
                count += (columns - j)
                start_j = j
                break

    return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid = [[3,2],[1,0]]
grid = [[1,-1],[-1,-1]]
grid = [[-1]]
print(countNegatives(grid))
