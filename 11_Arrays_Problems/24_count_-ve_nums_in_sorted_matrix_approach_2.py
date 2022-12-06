def countNegatives(grid):
    rows    = len(grid)
    columns = len(grid[0])

    count = 0
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] < 0:
                count += (columns - j)
                break

    return count


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# grid = [[3,2],[1,0]]
# grid = [[1,-1],[-1,-1]]
# grid = [[-1]]
print(countNegatives(grid))