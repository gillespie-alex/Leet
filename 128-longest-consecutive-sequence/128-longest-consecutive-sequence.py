class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        our_set = set(nums)
        res = 1
        for number in our_set:
            if number - 1 in our_set:
                continue
            else:
                temp = number
                cnt = 0
                # otherwise we are at the start of a set
                while temp in our_set:
                    cnt += 1
                    temp = temp + 1
                res = max(res, cnt)
        return res
                    