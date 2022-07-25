class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
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