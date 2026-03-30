class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 8]
        #  []
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        prefix_prod = 1
        for i in range(0, len(nums)):
            prefix[i] = prefix_prod
            prefix_prod *= nums[i]
        
        suffix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suffix_prod
            suffix_prod *= nums[i]
        
        result = []
        for i in range(0, len(nums)):
            result.append(prefix[i] * suffix[i])
        
        return result
        
        
