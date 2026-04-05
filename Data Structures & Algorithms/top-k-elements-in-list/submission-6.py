class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for i in range(len(nums) + 1)]

        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        for key, val in hm.items():
            counts[val].append(key)
        

        res = []
        print(counts)

        for i in range(len(counts)- 1, -1, -1):
            for it in counts[i]:
                if len(res) == k:
                    return res
                res.append(it)
        
        return res
        