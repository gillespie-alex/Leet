class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp bottom-up solution working from the end of the array
        dp = [False]*len(nums)
        dp[-1] = True
        for i in reversed(range(len(dp) - 1)):
            if True in dp[i: i + nums[i] + 1]:
                dp[i] = True
        return dp[0]
        