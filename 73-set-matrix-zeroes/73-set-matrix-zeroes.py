class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first I will find the location of the zero, then pass that location to a helper function
        
        def helper(Set):
            # will get all zeroes for these row and cols
            for coords in Set:
                row,col = coords
                for m in range(len(matrix)):
                    if m == row:
                        matrix[m] = list(map(lambda x: 0, matrix[m]))
                        continue
                    for n in range(len(matrix[0])):
                        if n == col:
                            matrix[m][n] = 0
        zeroes = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.add((i,j))
        helper(zeroes)
        #print(matrix)