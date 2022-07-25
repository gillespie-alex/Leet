class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+" : 1, "-" : 1, "*" : 1, "/" : 1}
        res = []
            
        def operation(sign, arg1, arg2):
            if sign == "+":
                return arg2 + arg1
            elif sign == "-":
                return arg2 - arg1
            elif sign == "*":
                return arg2 * arg1
            else:
                return int(arg2 / arg1)
        
        for char in tokens:
            if char in operators:
                arg1, arg2 = int(res.pop()), int(res.pop())
                res.append(operation(char, arg1, arg2))
            else:
                res.append(char)
        
        return res[-1]