class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        length = len(needle)
        iterator = 0
        while iterator < len(haystack):
            if haystack[iterator: iterator + length] == needle:
                return iterator
            iterator += 1
        return -1
        