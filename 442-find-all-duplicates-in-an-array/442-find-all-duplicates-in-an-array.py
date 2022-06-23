class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(len(nums)):
            x = abs(nums[i])-1
            if nums[x] < 0:
                res.append(abs(nums[i]))
            else:
                nums[x] *= -1
        return res
        