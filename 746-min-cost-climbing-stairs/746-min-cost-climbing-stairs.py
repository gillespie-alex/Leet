class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost.copy()
        dp.append(0)
        for i in reversed(range(len(dp) - 2)):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0],dp[1])