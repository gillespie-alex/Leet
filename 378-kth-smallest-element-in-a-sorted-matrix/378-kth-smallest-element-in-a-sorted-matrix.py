class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return
        heap = []
        for rows in matrix:
            heap.extend(rows)
        heapq.heapify(heap)
        for i in range(k-1):
            print(i)
            heapq.heappop(heap)
        return heapq.heappop(heap)        