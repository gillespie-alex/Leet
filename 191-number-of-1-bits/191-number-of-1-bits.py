class Solution:
    def hammingWeight(self, n: int) -> int:
        def Kernighan_algo(num):
            cnt = 0
            while num != 0:
                num &= (num -1)
                cnt += 1
            return cnt
        return Kernighan_algo(n)
        