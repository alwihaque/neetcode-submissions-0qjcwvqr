class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-c for c in counts.values()]
        heapq.heapify(max_heap)

        queue = collections.deque()
        time = 0
        print(max_heap)
        while max_heap or queue:
            time += 1
            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    queue.append([count, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return time

        