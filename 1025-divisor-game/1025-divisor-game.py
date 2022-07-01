class Solution:
    def divisorGame(self, n: int) -> bool:
        # bottom-up dynamic programming approach
        test = 0
        dp = [False] * n
        # we know these from the problem statments dp[1] = False & dp[2] = True
        for i in range(1,n):
            dp[i] = not dp[i-1]
        return dp[n-1]