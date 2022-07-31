class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Make a copy of the nums array and extend the original array to be twice as long
        # Then use a decreasing monotonic queue
        nums_len = len(nums)
        nums = nums + nums.copy()
        res = [-1] * nums_len * 2
        dec_queue = []
        for i in range(len(nums)):
            while dec_queue and nums[i] > nums[dec_queue[-1]]:
                index = dec_queue.pop()
                res[index] = nums[i]
            dec_queue.append(i)
        return res[0:nums_len]
                
        