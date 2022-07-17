class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}  #(total, index)
        def dfs(num, index):
            if index == len(nums) - 1:
                return 1 if num == target else 0
            elif (num, index) in cache:
                return cache[(num, index)]
            cache[(num, index)] = dfs(num + nums[index+1], index + 1) + \
                                    dfs(num - nums[index+1], index + 1)
            return cache[(num, index)]
        
        return dfs(nums[0], 0) + dfs(-nums[0],0)