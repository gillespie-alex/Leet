class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        fast = 0
        window = []
        sub = 0
        if not s:
            return 0
        while (fast != len(s)):
            if s[fast] in window:
                #clear the window up to the repeated character
                while (window[0] != s[fast]):
                    window.pop(0)
                window.pop(0)
                #append the new character
                window.append(s[fast])
                fast += 1
            else:
                window.append(s[fast])
                if len(window) > sub:
                    sub = len(window)
                fast += 1
        return sub
        