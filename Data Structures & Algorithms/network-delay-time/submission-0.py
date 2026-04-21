class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = defaultdict(list)

        for u, v, w in times:
            adj_list[u].append((v, w))
        
        minHeap = [(0, k)]
        visit = set()

        res = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            visit.add(n1)
            res = max(res, w1)
            
            for n2, w2 in adj_list[n1]:
                if not n2 in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
            
        return res if len(visit) == n else -1 


