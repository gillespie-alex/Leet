class Solution:
    def countBits(self, n: int) -> List[int]:
        bitmap = {0:0, 1:1, 2:1, 3:2}
        if n < 4:
            return [bitmap[i] for i in range(n+1)]
        dp = [0]*(n+1)
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 1, 2
        offset = 4
        for i in range(4,n + 1):
            if offset*2 == i:
                offset  = i
            dp[i] = 1 + dp[i - offset]
        return dp