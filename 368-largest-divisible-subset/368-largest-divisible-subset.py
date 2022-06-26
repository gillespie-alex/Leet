class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        dp = []
        nums.sort()
        dp.append([nums[0]])
        print(dp)
        for i in range(1,len(nums)):
            res = []
            for j in reversed(range(i+1)):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    if not res:
                        res.append(nums[i])
                        continue
                    if len(res) < 1 + len(dp[j]):
                        res = [nums[i]] + dp[j]
            dp.append(res) 
        subset = []
        sub_max = 1
        for i in range(len(dp)):
            if len(dp[i]) >= sub_max:
                sub_max = len(dp[i])
                subset = dp[i]
        return reversed(subset)