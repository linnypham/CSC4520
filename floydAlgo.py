def floyd(grid):
    m = len(grid)
    for k in range(m):  
        for i in range(m):  
            for j in range(m): 
                grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])
    return grid

def floydAlgo(grid):
    for i in range(len(grid)):
        floyd(grid)
    


grid = [[0,3,float('inf'),7],
        [8,0,2,float('inf')],
        [5,float('inf'),0,1],
        [2,float('inf'),float('inf'),0]]

floydAlgo(grid)
for line in grid:
    print(line)       

