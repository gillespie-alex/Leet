class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start, end = 0, 0
        dec = []
        inc = []
        res_max = 0
        for i in range(len(nums)):
            while inc and nums[i] <= nums[inc[-1]]:
                inc.pop()
            inc.append(i)
            while inc and inc[0] < start:
                inc.pop(0)
                
            # same process for decreasing
            while dec and nums[i] >= nums[dec[-1]]:
                dec.pop()
            dec.append(i)
            while dec and dec[0] < start:
                dec.pop(0)
            if nums[dec[0]] - nums[inc[0]] <= limit:
                res_max = max(res_max, end-start + 1)
            else:
                start += 1
            end += 1
        return res_max