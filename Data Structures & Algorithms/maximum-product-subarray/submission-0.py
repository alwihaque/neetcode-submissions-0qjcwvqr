class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_result = float('-inf')

        for i in range(len(nums)):
            j = i
            res = 1
            while j < len(nums):
                res *= nums[j]
                max_result = max(max_result, res)
                j += 1
        
        return max_result
            
        