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
            
               
        
        
