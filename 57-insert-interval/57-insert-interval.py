class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        # first find a place to add the interval
        ptr = 0
        elem = newInterval
        while elem > intervals[ptr]:
            ptr += 1
            if ptr >= len(intervals):
                break
        intervals.insert(ptr, elem)
        
        res = []
        for lists in intervals:
            if not res:
                res.append(lists)
                continue
            if lists[0] >= res[-1][0] and lists[0] <= res[-1][1]:
                # update result
                res[-1][1] = lists[1] if lists[1] > res[-1][1] else res[-1][1]
            else:
                res.append(lists)
        return res