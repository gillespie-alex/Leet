class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = set()
        ugly_nums.add(1)
        heap = [1]    
        for i in range(1,n):
            multiplier = heapq.heappop(heap)
            x = 2*multiplier
            y = 3*multiplier
            z = 5*multiplier
            if x not in ugly_nums:
                ugly_nums.add(x)
                heapq.heappush(heap,x)
            if y not in ugly_nums:
                ugly_nums.add(y)
                heapq.heappush(heap,y)
            if z not in ugly_nums:
                ugly_nums.add(z)
                heapq.heappush(heap,z)    
        return heapq.heappop(heap)

        