class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        sums = set()
        sums.add(nums[0])
        for i in range (1, len(nums)):
            copy = sums.copy()
            sums.add(nums[i])
            for stuff in copy:
                sums.add(nums[i] + stuff)
        target = sum(nums) // 2
        return True if target in sums else False
