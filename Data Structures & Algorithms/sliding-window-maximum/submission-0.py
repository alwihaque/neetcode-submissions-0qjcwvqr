class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []

        while r < len(nums):
            max_val = nums[l]
            for i in range(l, r + 1):
                max_val = max(max_val, nums[i])
            l += 1
            r += 1
            res.append(max_val)
        return res    

            
            
        