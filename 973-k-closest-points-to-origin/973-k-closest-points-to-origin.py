class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # first heapify the List
        heap = []
        for coords in points:
            # calculate euclidian distance
            x,y = coords[0],coords[1]
            val = sqrt(x**2+y**2)
            heapq.heappush(heap,(val,coords))
        res = []
        for i in range(k):
            a,b = heapq.heappop(heap)
            res.append(b)
        return res