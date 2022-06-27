class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
    
        # will be passed as a tuple
        def dfs(root):
            row,col = root
            left,right =  triangle[row][col], triangle[row][col]

            if (row,col) in memo:
                return memo[row,col]

            if row + 1 < len(triangle):
                left += dfs((row + 1, col))
                if col + 1 < len(triangle[row + 1]):
                    right += dfs((row + 1, col + 1))

            M = min(left,right)

            # memoify the result 
            memo[(row,col)] = M
            return M

        start = (0,0)
        return dfs(start)
        