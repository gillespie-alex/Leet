class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, val in enumerate(nums):
            if target - val in mapping:
                return [i, mapping[target - val]]
            mapping[val] = i