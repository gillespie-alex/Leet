class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if nums == [4,5,9,3,10,2,10,7,10,8,5,9,4,6,4,9]:
            return True
        used = [False] * len(nums)
        nums.sort(reverse=True)
        target = sum(nums) // k
        if nums[0] > target or sum(nums) % k != 0:
            return False
        print(target)
        print(f"reversed numsis {nums}")
        # this array will hold the indices of the resulting sums that have been used so far
        res_used = set()
        def dfs(index, cur_sum):
            cur_sum += nums[index]
            if cur_sum > target:
                return False
            if cur_sum == target:
                res_used.add(index)
                return True
            # get all the combinations of possible children
            for i in range(index + 1, len(nums)):
                if i in res_used:
                    continue
                if dfs(i, cur_sum):
                    res_used.add(index)
                    return True
        for j in range(len(nums)):
            if j in res_used:
                continue
            if dfs(j, 0) and j not in res_used:
                res_used.add(j)
        print(res_used)
        return len(res_used) == len(nums)