class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def bin_search(arr, t):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == t:
                    return mid
                if arr[mid] < t:
                    left = mid + 1
                else:
                    right = mid - 1
            return -999
        for i, val in enumerate(nums):
            temp = bin_search(nums[i+1:], target - val)
            if temp != -999:
                return [i+1,temp+i+2]