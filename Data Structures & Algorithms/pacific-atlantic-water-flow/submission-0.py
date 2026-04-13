class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        def dfs(r, c, max_height, visited):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or heights[r][c] < max_height:
                return
            
            visited.add((r, c))

            directions = [[1,0], [-1,0], [0,1], [0, -1]]

            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], visited)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs((ROWS - 1), c, heights[ROWS - 1][c], atlantic)
        

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)
        
        res = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlantic and (r, c) in pacific:
                    res.append([r,c])
        
        return res






        