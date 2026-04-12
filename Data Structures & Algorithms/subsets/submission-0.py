class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets, curr_set = [], []
        i = 0

        def helper(i, nums, subset, curr_set):
            if i >= len(nums):
                subsets.append(curr_set.copy())
                return
            
            curr_set.append(nums[i])
            helper(i + 1, nums, subset, curr_set)
            curr_set.pop()
            helper(i + 1, nums, subset, curr_set)
        
        helper(i, nums, subsets, curr_set)
        return subsets
        