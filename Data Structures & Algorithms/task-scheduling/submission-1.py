class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter(tasks)

        max_heap = [-count for count in counts.values()]

        heapq.heapify(max_heap)

        time = 0

        queue = collections.deque()

        while queue or max_heap:
            time += 1

            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    queue.append([count, time + n])
            
            if queue and queue[0][1] == time:
                item = queue.popleft()
                heapq.heappush(max_heap, item[0])
        
        return time

        