class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp_min = [0]*len(nums)
        dp[0] = nums[0]
        dp_min[0] = nums[0]
        max_num = dp[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i], nums[i]*dp[i-1], nums[i]*dp_min[i-1])
            dp_min[i] = min(nums[i], nums[i]*dp_min[i-1], nums[i]*dp[i-1])
            max_num = max(max_num, dp[i], dp_min[i])
        return max_num