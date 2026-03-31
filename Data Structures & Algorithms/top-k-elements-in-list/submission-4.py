class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = {}
        count = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        for key, v in hm.items():
            count[v].append(key)
        
        result = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                result.append(num)
                if len(result) == k:
                    return result
            


        