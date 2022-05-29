class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return
        slow = 0
        for fast in range(len(nums)):
            if (nums[slow] != nums[fast]) and (fast - slow > 1):
                slow += 1
                nums[slow] = nums[fast]
            if (nums[slow] != nums[fast]) and (fast - slow == 1):
                slow += 1
        return slow+1