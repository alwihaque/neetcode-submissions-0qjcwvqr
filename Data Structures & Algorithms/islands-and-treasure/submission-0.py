class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

       


        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()

        def addRoom(r, c):

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or (r, c) in visited):
                return
            
            visited.add((r,c))
            queue.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    addRoom(r + dr, c + dc)
                
            dist += 1


        