class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj_list = {i:[] for i in range(n)}

        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
        
        
        def dfs(curr):            
            for neighbor in adj_list[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        num_connected = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                num_connected += 1
        
        return num_connected
        

        
        
        