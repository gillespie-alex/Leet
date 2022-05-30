class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        #first convert the string to all lowercase
        string = s.lower()
        left, right = 0, len(string)-1
        while left < right:
            while string[right].isalnum() is False and (left < right):
                right -= 1
            while string[left].isalnum() is False and (left < right):
                left += 1
            #now both of the pointers are pointing to non-whitespace characters
            if string[left] != string[right]:
                return False
            #otherwise move the pointer
            left += 1
            right -= 1
        return True
        