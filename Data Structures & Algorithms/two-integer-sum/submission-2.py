class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in hm:
                return [hm[complement], index]
            
            hm[num] = index
        
        return None
        