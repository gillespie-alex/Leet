class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0]*n
        dp[-1] = 1
        dp[-2] = 2
        for i in reversed(range(n-2)):
            dp[i] = dp[i+1] + dp[i+2]
        return dp[0]
        