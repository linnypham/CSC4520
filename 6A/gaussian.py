def gaussian(grid):
    m = len(grid)
    n = len(grid[0])
    def triangle(grid):
        for i in range(1,m):
            for j in range(i):
                if grid[i][j]!=0:
                    return False
    while not triangle(grid):
        for i in range(1,m):
            for j in range(n):
                coefficient = grid[i][j]/grid[0][0]
                grid[i][j] = grid[i][j] - coefficient*grid[0][j]
    

grid = [[2,-1,1,1],[4,1,-1,5],[1,1,1,0]]
gaussian(grid)
print(grid)