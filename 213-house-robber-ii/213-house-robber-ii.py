class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        def house_robber_i(arr):
            dp = [0]*(len(arr))
            dp[0], dp[1] = arr[0], max(arr[0], arr[1])
            for i in range(2,len(dp)):
                dp[i] = max(dp[i-1], arr[i] + dp[i-2])
            return dp[-1]
        
        return max (house_robber_i(nums[1:]), house_robber_i(nums[:-1]))