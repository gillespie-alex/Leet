class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # compare each string from left to right (or right to left doesn't matter)
        memo = {}
        def dfs(s1, s2, LCS):
            if not s1 or not s2:
                return 0
            if (s1,s2) in memo:
                return memo[(s1,s2)]
            elif s1[-1] == s2[-1]:
                LCS += dfs(s1[0:-1], s2[0:-1], LCS) + 1
            else:
                LCS += max(dfs(s1, s2[0:-1], LCS), dfs(s1[0:-1], s2, LCS))
            memo[(s1,s2)] = LCS
            return memo[(s1,s2)]
        return dfs(text1, text2, 0)