class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force

        max_k = max(piles)

        # for i in range(1, max_k + 1):
        #     total_time = 0
        #     for pile in piles:
        #         total_time += math.ceil(float(pile)/i)
            
            
        #     if total_time <= h:
        #         return i

        l, r = 1, max(piles)
        result = 0
        while l <= r:
            k = (l + r)//2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p)/k)
            
            if total_time > h:
                l = k + 1
            else:
                result = k
                r = k - 1
        
        return result
                




        