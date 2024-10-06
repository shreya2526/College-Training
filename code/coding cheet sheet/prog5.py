def paths(grid):
    
    if not grid or grid[0]==1:
        return 0
    
    m,n=len(grid),len(grid[0])
    
    dp=[[0]*n for _ in range (m)]
    
    dp[0][0]=1
    
    for j in range(1,n):
        dp[0][j]=1 if grid[0][j]==0 and dp[0][j-1]==1 else 0
    
    for i in range(1,m):
        dp[i][0]=1 if grid[i][0]==0 and dp[i-1][0]==1 else 0

    for i in range(1,m):
        for j in range(1,n):
            if grid[i][j]==0:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
            else:
                dp[i][j]=0

    return dp[m-1][n-1]

# grid=[[0,0,0],
#       [0,1,0],
#       [0,0,0]]
grid=[[0,1],[0,0]]
print(paths(grid))