class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # this is similar to the coin change problem
        dp = [0]*(target+1)
        if 0 in nums:
            dp[0] = 1
        for i in range(1, target + 1):
            if i in nums:
                dp[i] += 1
            for vals in nums:
                if i - vals > 0:
                    dp[i] += dp[i - vals]
        return dp[-1]