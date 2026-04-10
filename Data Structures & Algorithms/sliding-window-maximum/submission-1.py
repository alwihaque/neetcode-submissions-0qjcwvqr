class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        for i in range((len(nums) - k) + 1):
            window_start = i 
            window_end = i + k

            max_val = max(nums[window_start:window_end])
            results.append(max_val)
        return results        