class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negatives =[- n for n in nums]
        heapq.heapify(negatives)

        i = 1
        
        while i < k:
            heapq.heappop(negatives)
            i+= 1
        
        return heapq.heappop(negatives) * -1
        

