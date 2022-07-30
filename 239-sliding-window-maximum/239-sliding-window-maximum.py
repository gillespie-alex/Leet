class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(n) solution using a monotonic decreasing queue
        dec_queue = []
        # fill up the queue for the first window
        for i in range(k):
            while dec_queue and nums[i] > nums[dec_queue[-1]]:
                dec_queue.pop()
            dec_queue.append(i)
        res = []
        res.append(nums[dec_queue[0]])
        for i in range(1, len(nums) - k + 1):
            new_val = nums[i + k - 1]
            while dec_queue and new_val > nums[dec_queue[-1]]:
                dec_queue.pop()
            dec_queue.append(i + k - 1)
            while dec_queue[0] < i:
                dec_queue.pop(0)
            res.append(nums[dec_queue[0]])
        return res