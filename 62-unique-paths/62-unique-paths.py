class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # I want to use a matrix and have each square represent how many unique paths
        # there are up to that specifc square so far seen, and the final square will
        # represent the sum of all unique paths as its top and left neighbors hold all
        # the unique paths to that square, so we just add those to get the final answer
        
        rows,cols = m, n
        # initialize all to 1 cuz first row and first column can only have 1 unique path
        dp = [[1 for i in range(cols)] for j in range(rows)]
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j] = max(dp[i][j], dp[i-1][j] + dp[i][j-1])
        return dp[-1][-1]
        