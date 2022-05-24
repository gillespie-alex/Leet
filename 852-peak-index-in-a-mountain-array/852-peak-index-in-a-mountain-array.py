class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        low = 0
        high = len(arr)-1
        return self.bin_search(arr, low, high)
    def bin_search(self, arr, low, high):
            if high == low:
                return low
            else:
                mid = (high + low) // 2
                if (arr[mid+1]) > arr[mid]:
                    return self.bin_search(arr, mid+1, high, )
                else:
                    return self.bin_search(arr, low, mid)
            
               
        
        
# low = 0
#         high = len(nums)-1
#         return self.bin_search( nums, low, high, target)
#     def bin_search(self, arr, low, high, x):
#         if high>= low:
#             mid = (high + low)//2
#             if arr[mid] == x:
#                 return mid
#             elif arr[mid] > x:
#                 return self.bin_search(arr, low, mid -1, x)
#             else:
#                 return self.bin_search(arr, mid + 1, high, x)
#         else:
#             return -1