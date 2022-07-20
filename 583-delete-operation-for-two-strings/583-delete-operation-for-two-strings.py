class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        # preset the first row and first col
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
        
        # filling rest of dp matrix
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        