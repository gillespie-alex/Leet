class Solution:
    def countSubstrings(self, s: str) -> int:
        # there are two cases to be taken care of:
        # 1. the length of palindrome is odd
        # 2. the length of the palindrome is even
        
        pal_cnt = 0
        
        # 1. Odd Case
        for i in range(len(s)):
            l,r = i,i
            while s[l] == s[r]:
                pal_cnt += 1
                l -= 1
                r += 1
                if l < 0 or r >= len(s):
                    break
        
        # 2. Even Case
        for i in range(len(s) - 1):
            l,r = i,i+1
            while s[l] == s[r]:
                print(s[l],s[r])
                pal_cnt += 1
                l -= 1
                r += 1
                if l < 0 or r >= len(s):
                    break
        return (pal_cnt)