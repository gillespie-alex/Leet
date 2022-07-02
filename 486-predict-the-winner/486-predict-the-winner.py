class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # this will be a bottom-up DP approach
        size = len(nums)
        dp = [[0 for _ in nums] for _ in nums]
        for i,val in enumerate(nums):
            dp[i][i] = val
        
        # recurrence relation is dp[i][j] = max(nums[i] + 
        # will start with length of 1 for sub-problem then to 3 and 4...
        for window in range(1, len(nums)):
            for j in range(0, size - window):
                if window == 1:
                    dp[j][j + window] = max(dp[j][j], dp[j + window][j + window])
                else:
                    dp[j][j + window] = max((dp[j][j] + sum(nums[j+1:j+window+1]) - dp[j+1][j+window]), \
                                           dp[j+window][j+window] + sum(nums[j:j+window]) - dp[j][j+window-1])
        
        return ((sum(nums) - dp[0][size-1]) <= dp[0][size-1])