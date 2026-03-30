class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        freq = [[] for i in range(len(nums) + 1)]


        for i in nums:
            hm[i] = hm.get(i, 0) + 1
        
        for key, val in hm.items():
            freq[val].append(key)

        res = []
        print(freq)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        




        