class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return -1
        length = len(nums)
        left, right = 0, length
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            for element in nums:
                if element <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return left