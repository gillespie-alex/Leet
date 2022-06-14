class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def get_puzzles(current):
            res = []
            # first find where the zero is 
            zero_loc = (0,0)
            for i in range(len(current)):
                for j in range(len(current[i])):
                    if current[i][j] == 0:
                        zero_loc = (i,j)
                        
            x,y = zero_loc
            # do stuff here to find all the neighbors of the blank space in the puzzle board
            row_offsets = [-1,0,1,0]
            col_offsets = [0,1,0,-1]
            for i in range(4):
                boards = copy.deepcopy(current)
                new_x = x + row_offsets[i]
                new_y = y + col_offsets[i]
                if new_x >= 0 and new_x <= 1 and new_y >= 0 and new_y <= 2:
                    # if this true then the new location for the zero is allowable so we flip-flop the value locations
                    boards[x][y], boards[new_x][new_y] = boards[new_x][new_y], boards[x][y] 
                    res.append(boards)
            return res
        def BFS(start):
            queue = ([start])
            used = ([start])
            moves = 0
            while len(queue) > 0:
                # first pop the current board
                for i in range(len(queue)):
                    board = queue.pop(0)
                    if board == [[1,2,3],[4,5,0]]:
                        return moves
                    for puzzle in get_puzzles(board):
                        # if the specifc puzzle configuration already exists then we have already checked
                        # it in past and no need to check it again
                        if puzzle in used:
                            continue
                        queue.append(puzzle)
                        used.append(puzzle)
                moves += 1
            return -1
        return BFS(board)
        