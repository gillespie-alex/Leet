class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = set()
        ugly_nums.add(1)
        factors = [2,3,5]
        heap = [1]    
        for i in range(1,n):
            multiplier = heapq.heappop(heap)
            for uglies in factors:
                if uglies*multiplier not in ugly_nums:
                    ugly_nums.add(uglies*multiplier)
                    heapq.heappush(heap,uglies*multiplier)
        return heapq.heappop(heap)

        