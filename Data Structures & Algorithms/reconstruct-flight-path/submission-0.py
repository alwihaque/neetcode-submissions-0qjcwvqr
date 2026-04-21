class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj_list = defaultdict(list)

        for departure, arrival in tickets:
            adj_list[departure].append(arrival)

        result = ['JFK']


        def dfs(src):
            if len(result) == len(tickets) + 1:
                return True
            
            if src not in adj_list:
                return False
            
            temp = list(adj_list[src])
            for i, v in enumerate(adj_list[src]):
                adj_list[src].pop(i)
                result.append(v)
                
                if dfs(v):
                    return True
                
                adj_list[src].insert(i, v)
                result.pop()
            
            return False
        
        dfs('JFK')
        return result


        