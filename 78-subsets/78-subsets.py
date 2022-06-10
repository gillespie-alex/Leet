class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(subset: List[int],  start: int):
            if subset not in res:
                subset_copy = subset.copy()
                res.append(subset_copy)
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i+1)
                subset.pop()
        res.append([])
        backtrack([], 0)
        return res
