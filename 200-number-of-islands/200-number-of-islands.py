class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        def get_island_neighbors(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    if grid[neighbor_row][neighbor_col] == "1":
                        grid[neighbor_row][neighbor_col] = "-1"
                        yield neighbor_row, neighbor_col
        
        def bfs_island(coordinates):
            queue = deque([coordinates])
            visited = set([coordinates])
            while len(queue) > 0:
                node = queue.popleft()
                for neighbor in get_island_neighbors(node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
        # this approach will probably be inefficient
        x,y = 0,0
        islands = 0
        for i,row in enumerate(grid):
            for j, col in enumerate(row):
                grid[i][j]
                coord = (i,j)
                if grid[i][j] == "1":
                    bfs_island(coord)
                    islands += 1
                elif grid[i][j] == "0":
                    grid[i][j] = "-1"
        return islands
        