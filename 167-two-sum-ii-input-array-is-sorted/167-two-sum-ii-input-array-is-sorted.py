class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            allowed = target - nums[l]
            while nums[r] > allowed:
                r -= 1
            if nums[r] == allowed:
                return [l+1, r+1]
            l += 1