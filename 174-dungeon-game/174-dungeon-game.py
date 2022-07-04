class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # find the minimum health to reach each position in the matrix
        dp = [[0 for cols in dungeon[0]] for rows in dungeon]
        m = len(dungeon)
        n = len(dungeon[0])
        dp[m-1][n-1] = (abs(dungeon[m-1][n-1]) + 1) if dungeon[m-1][n-1] < 0 else 1
        for i in range(len(dungeon) - 1, -1, -1):
            for j in range(len(dungeon[0]) - 1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                elif i == m-1:
                    dp[i][j] = 1 if dungeon[i][j] >= dp[i][j+1] else dp[i][j+1] - dungeon[i][j]
                elif j == n-1:
                    dp[i][j] = 1 if dungeon[i][j] >= dp[i+1][j] else dp[i+1][j] - dungeon[i][j]
                else:
                    down = max(dp[i+1][j] - dungeon[i][j], 1)
                    right = max(dp[i][j+1] - dungeon[i][j], 1)
                    dp[i][j] = min(down, right)
        return dp[0][0]