class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        hs = set()
        for num in nums:
            if num not in hs:
                hs.add(num)
        result = 1
        print(hs)
        for num in nums:
            candidate = num + 1
            length = 1
            while candidate in hs:
                length += 1
                result = max(length, result)
                candidate = candidate + 1
        return result



