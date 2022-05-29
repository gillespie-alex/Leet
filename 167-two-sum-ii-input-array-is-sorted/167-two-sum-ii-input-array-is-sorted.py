class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = numbers
        right = len(nums) - 1
        left = 0
        while left is not right:
            sums = nums[left] + nums[right]
            print(sums)
            if sums > target:
                right = right - 1
            if sums < target:
                left = left + 1
            if sums == target:
                break
        return left+1,right+1
        