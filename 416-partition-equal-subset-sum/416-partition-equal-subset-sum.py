class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums) // 2

        if sum(nums) % 2 != 0 or max(nums) > target:
            return False

        used = [False] * n

        @lru_cache(None)
        def dfs(cur_sum):
            if cur_sum == target:
                return True
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                if dfs(cur_sum + nums[i]):
                    return True
                used[i] = False
            return False
        return dfs(0)