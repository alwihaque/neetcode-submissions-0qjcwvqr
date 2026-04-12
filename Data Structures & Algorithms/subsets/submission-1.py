class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res, sub_sets = [], []
        i = 0

        def helper(i, sub_sets, nums):
            if i >= len(nums):
                res.append(sub_sets.copy())
                return
            
            sub_sets.append(nums[i])
            helper(i+1, sub_sets, nums)
            sub_sets.pop()
            helper(i+1, sub_sets, nums)
        
        helper(i, sub_sets, nums)
        return res
        