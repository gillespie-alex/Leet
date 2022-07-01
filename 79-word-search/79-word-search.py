class Solution:
    def exist(self, board: List[List[str]], word: str, RESULT = 0) -> bool:
        used = [[False for slots in board[0]] for rows in board]
        height = len(board)
        width = len(board[0])
        def get_children(coord):
            i,j = coord
            res = []
            row = [-1, 0 , 1, 0]
            col = [0, 1, 0, -1]
            for z in range(4):
                new_row = i + row[z]
                new_col = j + col[z]
                if new_row >= 0 and new_row < height and new_col >= 0 and new_col < width:
                    res.append((new_row, new_col))
            #print(f"origin coord {coord} and neighbors is {res}")
            return res  
        def dfs(coord, str_index):
            i,j = coord
            nonlocal RESULT
            if str_index == len(word) - 1:
                #print("here")
                RESULT += 1
                return
            for children in get_children(coord):
                x,y = children
                if used[x][y]:
                    continue
                if board[x][y] != word[str_index + 1]:
                    continue
                used[x][y] = True
                dfs(children, str_index + 1)
                used[x][y] = False   
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    used[i][j] = True
                    dfs((i,j),0)
                    used[i][j] = False
        return (RESULT >= 1)