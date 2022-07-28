class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def dfs(index, sub):
            if len(sub) == len(s):
                res.append(sub)
                return
            # for i in range(index, len(s)):
            if s[index] in string.ascii_letters:
                dfs(index + 1, sub + s[index].lower())
                dfs(index + 1, sub + s[index].upper())
            else:
                dfs(index + 1, sub + s[index])
        dfs(0, "")
        return res