class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curr_set = [], []
        i = 0

        def helper(i, nums, subsets, curr_set):
            if i >= len(nums):
                subsets.append(curr_set.copy())
                return
            
            curr_set.append(nums[i])
            helper(i + 1, nums, subsets, curr_set)
            curr_set.pop()
            while(i + 1 < len(nums) and nums[i] == nums[i+1]):
                i += 1
            
            helper(i + 1, nums, subsets, curr_set)

        helper(i, nums, subsets, curr_set)
        return subsets
        