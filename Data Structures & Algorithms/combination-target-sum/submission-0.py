class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(i, nums, target, sub_list):
            

            if sum(sub_list) >= target:
                if sum(sub_list) == target:
                    res.append(sub_list.copy())
                return
            
            for i in range(i, len(nums)):
                sub_list.append(nums[i])
                helper(i, nums, target, sub_list)
                sub_list.pop()
            
        
        helper(0, nums, target, [])
        return res
        