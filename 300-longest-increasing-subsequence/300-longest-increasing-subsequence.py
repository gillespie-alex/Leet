class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # helper function used to clean code and accomplishes the following:
        # looks for all possible previous subsequences that we can add the current dp[i] to

        def helper(end_range:int, dp_list: List[int]):
            subs = 1
            for i in range(end_range):
                if nums[end_range] > nums[i]:
                    subs = max(subs,1 + dp_list[i])
            return subs
        
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            dp[i] = helper(i,dp)
        return max(dp)
        