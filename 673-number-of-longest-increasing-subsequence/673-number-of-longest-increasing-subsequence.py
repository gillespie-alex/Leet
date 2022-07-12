class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {} # key = index, value = [length of LIS, count]
        lenLIS, res = 0, 0 # length of LIS, count of LIS
        
        # i = start of subseq
        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCnt = 1, 1 # len, cnt of LIS start from i
            
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j] # len, cnt of LIS start from j
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            dp[i] = [maxLen, maxCnt]
                
        return res