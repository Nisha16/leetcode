def search(i, j, grid, mark):
    mark[i][j] = False
     
    if i+1 < len(grid) and grid[i+1][j] == 1 and mark[i+1][j] == True:
        search(i+1,j,grid,mark)
         
    if j+1 < len(grid[0]) and grid[i][j+1] == 1 and mark[i][j+1] == True:
        search(i,j+1,grid,mark)
         
    if i-1 >= 0 and grid[i-1][j] == 1 and mark[i-1][j] == True:
        search(i-1,j,grid,mark)
         
    if j-1 >=0 and grid[i][j-1] == 1 and mark[i][j-1] == True:
        search(i,j-1,grid,mark)
     
    # @param {character[][]} grid
    # @return {integer}
def numIslands(grid):
    row = len(grid)
    if row == 0:
        return 0
    col = len(grid[0])
     
    #mark = [x[:] for x in [[True]*col]*row]
    mark = [[True for x in range(col)] for x in range(row)]
    print "mark ", mark
     
    res  = 0
    for i in range(0,row):
        for j in range(0, col):
            if grid[i][j] == 1 and mark[i][j] == True:
                search(i, j, grid,mark)
                res += 1
                print "mark1: ", mark
                print "res: ", res
    return res


grid = [[1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]]

grid1 = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]]        

print numIslands(grid1)        




