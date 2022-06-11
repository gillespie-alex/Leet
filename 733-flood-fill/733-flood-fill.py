class Solution:
    def floodFill(self, image: List[List[int]], r: int, c: int, replacement: int) -> List[List[int]]:
        num_rows = len(image)
        num_cols = len(image[0])
        original_color = image[r][c]  # this holds the original pixel color
        image[r][c] = replacement
        def helper(coordinates):
            row,col = coordinates
            # array of tuples holding all the neighbors to be found 
            res = []
            delta_rows = [-1,0,1,0]
            delta_cols = [0,1,0,-1]
            # iterate over one the offset lists
            for i in range(len(delta_rows)):
                neighbor_row = row + delta_rows[i]
                neighbor_col = col + delta_cols[i]
                # now I need to check whether this is in the range of the given matrix
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    res.append((neighbor_row, neighbor_col))
            return res
        def BFS(start):
            queue = deque([start])
            visited = set([start])
            while len(queue) > 0:
                node = queue.popleft()
                # node holds the coordinates of its location in the input matrix 
                for neighbor in helper(node):
                    if neighbor in visited:
                        continue
                    neighbor_x, neighbor_y = neighbor
                    if image[neighbor_x][neighbor_y] == original_color:
                        image[neighbor_x][neighbor_y] = replacement
                        queue.append(neighbor)
                        visited.add(neighbor)
        BFS((r,c))
        return image
