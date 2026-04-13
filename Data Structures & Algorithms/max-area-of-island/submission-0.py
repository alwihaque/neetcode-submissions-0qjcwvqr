class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_size = 0


        def dfs(r, c):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            size = 1
            visited.add((r, c))
            for dr, dc in directions:
                size += dfs(r + dr, c + dc)
            
            return size


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_size = max(max_size, dfs(r, c))
        
        return max_size
        