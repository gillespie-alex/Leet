class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using a min-heap, so to get the largest value we want the the inverse kth element
        if not nums:
            return
        res = len(nums) - k
        heapq.heapify(nums)
        print(nums)
        for i in range(res + 1):
            val = heapq.heappop(nums)
            if i == res:
                return val