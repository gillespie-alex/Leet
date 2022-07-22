class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # string = "abc"
        # x = string.startswith("a")
        memo = {}
        def dfs(s1_i, s2_i, s3_i):
            str1, str2 = True, True
            if (s1_i, s2_i, s3_i) in memo:
                return memo[(s1_i, s2_i, s3_i)]
            if s3_i >= len(s3) and s1_i >= len(s1) and s2_i >= len(s2):
                return True
            if s1_i >= len(s1):
                str1 = False
            if s2_i >= len(s2):
                str2 = False
            if (str1 and s3[s3_i:].startswith(s1[s1_i])) and (str2 and s3[s3_i:].startswith(s2[s2_i])):
                memo[(s1_i, s2_i, s3_i)] = dfs(s1_i + 1, s2_i, s3_i + 1) or dfs(s1_i, s2_i + 1, s3_i + 1)
            # only s1 can be used
            elif str1 and s3[s3_i:].startswith(s1[s1_i]):
                memo[(s1_i, s2_i, s3_i)] = dfs(s1_i + 1, s2_i, s3_i + 1)
            # only s2 can be used
            elif str2 and s3[s3_i:].startswith(s2[s2_i]):
                memo[(s1_i, s2_i, s3_i)] = dfs(s1_i, s2_i + 1, s3_i + 1)
            # neither can be used
            else:
                memo[(s1_i, s2_i, s3_i)] = False
            return memo[(s1_i, s2_i, s3_i)]
        return dfs(0,0,0)