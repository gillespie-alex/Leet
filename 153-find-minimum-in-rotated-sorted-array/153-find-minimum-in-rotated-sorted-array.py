class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            # if this is true then I know there is an inflection point somewhere on the right side
            if abs(left-right) == 1:
                return min(nums[left],nums[right])
            elif nums[right] - nums[mid] < 0:
                left = mid
            else:
                right = mid
        return nums[left]
        