class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        def Kernighan_algo(num):
            cnt = 0
            while num != 0:
                num &= (num -1)
                cnt += 1
            return cnt
        for i in range(n+1):
            res[i] = (Kernighan_algo(i))
        return res