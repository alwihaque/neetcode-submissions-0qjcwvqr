class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res, sub_sets = [], []
        i = 0

        def dfs(i, sub_sets, nums):
            if i >= len(nums):
                res.append(sub_sets.copy())
                return
            
            sub_sets.append(nums[i])
            dfs(i + 1, sub_sets, nums)
            sub_sets.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                
            
            dfs(i + 1,  sub_sets, nums)
        
        dfs(i, sub_sets, nums)
        return res

        