class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def helper(end_range:int, dp_list: List[int]):
            possibilities = []
            for i in range(end_range):
                # if the number for a specific dp is less than the current end_range's val then we add to subsequence
                # nums[i] vs nums[end_range]
                if nums[end_range] > nums[i]:
                    # if this is true update the max subsequence at this dp position
                    possibilities.append(1 + dp_list[i])
            return 1 if not possibilities else max(possibilities)



            # compare the dp indices if they are valid to become subsequence
        if not nums:
            return 0
        # every number of the array will have at least a subsequence of 1
        dp = [1] * len(nums)
        for i in range(1,len(nums)):
            dp[i] = helper(i,dp)
        return max(dp)
        