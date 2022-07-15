class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        # for each day check the max profit that can be had before that day, and max after 
        # return the max of this DP array
        
        dp_cur = [0]*len(nums)
        min_seen = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < min_seen:
                min_seen = nums[i]
            dp_cur[i] = nums[i] - min_seen if nums[i] - min_seen > dp_cur[i-1] else dp_cur[i-1]
        
        dp_post = [0]*len(nums)
        max_seen = nums[-1]
        for j in reversed(range(len(nums) - 1)):
            if nums[j] > max_seen:
                max_seen = nums[j]
            dp_post[j] = max_seen - nums[j] if max_seen - nums[j] > dp_post[j+1] else dp_post[j+1]
        return max([dp_cur[i] + dp_post[i] for i in range(len(nums))])
        