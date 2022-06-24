class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # because we can only move down or right we can compute the top row and left columns manually
        for i in range(len(grid)):
            if i == 0:
                for j in range(1,len(grid[i])):
                    grid[i][j] += grid[i][j-1] 
            else:
                grid[i][0] += grid[i-1][0]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]