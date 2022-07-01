class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        max_prof = 0
        while r < len(prices) - 1:
            r += 1
            max_prof = max(max_prof, prices[r]-prices[l])
            if prices[r] < prices[l]:
                l = r
        return max_prof
                