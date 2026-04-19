class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x1, y1 in points:
            distance = math.sqrt(x1**2 + y1 **2 )
            min_heap.append((distance * - 1, x1, y1))
        
        print(min_heap)
        heapq.heapify(min_heap)

        while len(min_heap) > k:
            heapq.heappop(min_heap)
        
        res = []

        for _,x, y in min_heap:
            res.append([x,y])
        
        return res

            
        