class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # brute force
        for i, n in enumerate(nums):
            if n == target:
                return i
        
        return -1
        