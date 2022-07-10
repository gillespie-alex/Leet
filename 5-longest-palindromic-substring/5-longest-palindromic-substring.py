class Solution:
    def longestPalindrome(self, s: str) -> str:
        # I am going to use a 2-D DP array representing the length of the substring
        dp = [[False for _ in s] for _ in s]
        longest = (0,0)
        for i in range(0, len(s)):
            for j in range(0,len(s)-i):
                l,r = s[j], s[j+i]
                #sub = s[j:j+i+1]
                if i == 0 or i == 1:
                    if l == r:
                        dp[j][j+i] = True
                        longest = (j,j+i+1)#s[j:j+i+1]
                else:
                    # if this is true check the sub-coords 
                    if l == r:
                        if dp[j+1][j+i-1]:
                            dp[j][j+i]=True
                            #sub = s[j:j+i+1]
                            longest = (j,j+i+1) #sub if len(sub) > len(longest) else longest
        start,finish = longest
        return s[start:finish]