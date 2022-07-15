class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP solution where the only factors in decision-making are previous day and current
        # if current-prev is negative, dp is 0, sum dp array after
        dp = [0]*len(prices)
        net_prof = 0
        for i in range(1,len(prices)):
            current_prof = prices[i] - prices[i-1]
            dp[i] = current_prof if current_prof > 0 else 0
            net_prof += dp[i]
        return net_prof