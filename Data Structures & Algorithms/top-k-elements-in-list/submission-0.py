class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        frequencies = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)

        for n, v in hm.items():
            frequencies[v].append(n)

        result = []
        for i in range(len(frequencies) - 1, 0, -1):
            for n in frequencies[i]:
                result.append(n)
                print(len)
                if len(result) == k:
                    return result        
        