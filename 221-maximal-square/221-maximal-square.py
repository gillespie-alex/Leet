class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # first I want to create my cache
        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[0 for i in range(cols)] for j in range(rows)]
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == len(matrix)-1:
                    if int(matrix[i][j]) == 1: max_area = 1
                    memo[i][j] = int(matrix[i][j])
                elif j == len(matrix[i])-1:
                    if int(matrix[i][j]) == 1: max_area = 1
                    memo[i][j] = int(matrix[i][j])
        
        for i in reversed(range(len(matrix)-1)):
            for j in reversed (range(len(matrix[i])-1)):
                if matrix[i][j] == '0':
                    continue
                memo[i][j] = int(matrix[i][j]) + min(memo[i][j+1], memo[i+1][j], memo[i+1][j+1])
                if memo[i][j] > max_area:
                    max_area = memo[i][j]
        return max_area**2
                