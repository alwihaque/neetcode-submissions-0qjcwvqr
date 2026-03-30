class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}

        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in hm:
                return [hm[complement], i]
            else:
                hm[nums[i]] = i    
        