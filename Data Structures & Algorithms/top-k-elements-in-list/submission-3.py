class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = [[] for i in range(len(nums) + 1)]

        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        for key, value in hm.items():
            count[value].append(key)

        
        result = []

        print(count)
            
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                result.append(num)
                if len(result) == k:
                    return result 