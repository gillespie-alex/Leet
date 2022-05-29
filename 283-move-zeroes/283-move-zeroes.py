class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast != len(nums)-1:
            fast += 1
            while nums[slow] != 0:
                #in this case I want to move slow to a zeroed location
                slow += 1
                if slow == len(nums)-1: return nums
            if (nums[fast] != 0 and fast > slow):
                nums[slow] = nums[fast]
                nums[fast] = 0
        return nums
            