class Solution:
    def reverseWords(self, s: str) -> str:
        # first step is to align the first word
        l = r = len(s) - 1
        res = []
        while s[l] == ' ':
            l -= 1
            r -= 1
        while r >= 0:
            if l == r and l == 0:
                res.append(s[l:r+1])
                break
            
            # find the subwindow
            while l >= 0 and s[l] != ' ':
                l -= 1
            res.append(s[l+1:r+1])
            if l <= 0:
                break
            r = l
            while s[l] == ' ':
                l -= 1
                r -= 1
        return ' '.join(res)