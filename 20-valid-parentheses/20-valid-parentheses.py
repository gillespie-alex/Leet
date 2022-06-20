class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack appeding the inputs and popping only when most recent input 
        # is the correct inverse of the next incoming input
        # the queue must be empty in the end for it to be valid
        # answer is in O(n) time complexity and O(n) space complexity
        string = []
        string.extend(s)
        stack = deque()
        closings = {']':'[',
                    ')':'(',
                    '}':'{'}
        i = -1
        for character in string:
            i += 1
            stack.append(character)
            if len(stack) < 2 or character not in closings:
                continue
            if stack[i-1] == closings[character]:
                stack.pop()
                stack.pop()
                i -= 2
        return (len(stack) == 0)
        