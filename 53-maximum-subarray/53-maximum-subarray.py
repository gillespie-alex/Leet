class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp array from left to right where each element contains the max subarray seen at this point
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
        return max(dp)