class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def is_valid(parentheses):
            left_cnt = 0
            right_cnt = 0
            for parenth in parentheses:
                if parenth == '(':
                    left_cnt += 1
                else:
                    right_cnt += 1
            if right_cnt > left_cnt or left_cnt > n:
                return False
            return True
        def dfs(parentheses):
            if len(parentheses) == n*2:
                res.append(parentheses)
                return
            word1 = parentheses + ')'
            word2 = parentheses + '('
            if is_valid(word1):
                dfs(word1)
            if is_valid(word2):
                dfs(word2)
        dfs("")
        return res