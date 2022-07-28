class Solution:
    def jump(self, nums: List[int]) -> int:
        inf = float('inf')
        dp = [inf] * len(nums)
        dp[-1] = 0
        print(dp)
        for i in reversed(range(len(nums)-1)):
            if nums[i] == 0:
                continue
            # check for anything in the range of [1,nums[i]]
            else:
                temp_min = min(dp[i:i+nums[i]+1])
                dp[i] = 1 + temp_min    #dp[i+nums[i]]
        return dp[0]