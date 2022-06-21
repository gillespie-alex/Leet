class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i,element in enumerate(nums):
            nums[i] = abs(nums[i])
        heapq.heapify(nums)

        res = []
        while nums:
            res.append((heapq.heappop(nums))**2)
        return res