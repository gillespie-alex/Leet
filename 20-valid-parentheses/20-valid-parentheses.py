class Solution:
    def isValid(self, s: str) -> bool:
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
        