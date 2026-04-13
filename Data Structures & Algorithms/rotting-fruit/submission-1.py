class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        queue, visited = collections.deque(), set()

        def check_for_oranges(r, c):
            nonlocal good_oranges
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in visited:
                return 
            queue.append([r,c])
            visited.add((r,c))
            good_oranges -= 1




        good_oranges = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    good_oranges += 1
                
                elif grid[r][c] == 2:
                    queue.append([r, c])
                    visited.add((r,c))
        
        if good_oranges == 0:
            return 0
        
        time_elapsed = 0
        
        while queue:
            for i in range(len(queue)):
                (r,c) = queue.popleft()
                
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    check_for_oranges(r + dr, c + dc)
                
        
                    
            time_elapsed += 1

            if good_oranges == 0:
                return time_elapsed
        
        return -1

        