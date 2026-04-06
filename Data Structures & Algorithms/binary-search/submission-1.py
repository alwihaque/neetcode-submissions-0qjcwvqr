class Solution:
    def search(self, nums: List[int], target: int) -> int:

        r = len(nums) - 1
        l = 0
        

        while l <= r:
            
            m = (r + l) // 2
            print(m)
            print(nums[m])
            if nums[m] < target: 
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1
        