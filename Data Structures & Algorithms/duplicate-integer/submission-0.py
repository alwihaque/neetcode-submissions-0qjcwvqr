class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        hm = {}
        for i in range(0, len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                hm[nums[i]] += 1

        for value in hm.values():
            print(value)
            if value > 1:
                return True    
        return False
        