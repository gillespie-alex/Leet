class Solution:
    def numSquares(self, n: int) -> int:
        # LEETCODE IS DUMB AND ADDED TEST CASES SO DP SOLUTIONS AREN'T ALLOWED ANYMORE
        # Unless you use some sort of "static" DP approach which isn't common
        
        # squares = [i**2 for i in range(1,n) if i**2 <= n]
        # dp = [n]*(n+1)
        # dp[0], dp[1] = 0, 1
        # for i in range(1, n + 1):
        #     for perf in squares:
        #         dp[i] = i
        #         if i - perf < 0:
        #             break
        #         elif dp[i-1] == 1:
        #             dp[i] = 2
        #             continue
        #         dp[i] = min(dp[i], 1 + dp[i - perf])
        # print(dp)
        # return dp[-1]
        dp = [n] * (n + 1)
        dp[0] = 0
        
        squares = [x**2 for x in range(0, n) if x**2<=n]

        for target in range(1, n + 1):
            dp[target] = target
            for square in squares: 
                if target - square < 0: 
                    break
                dp[target] = min(dp[target], 1+dp[target-square])
        return dp[n]