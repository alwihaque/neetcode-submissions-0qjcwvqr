class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = [0] * len(height)
        max_r = [0] * len(height)
        max_so_far = 0
        for i, h in enumerate(height):
            max_l[i] = max_so_far
            max_so_far = max(max_so_far, h)

        max_so_far = 0
        for i in range(len(height) - 1, -1, -1):
            max_r[i] = max_so_far
            max_so_far = max(max_so_far, height[i])
        
        result = 0
        for i, h in enumerate(height):
            water = min(max_l[i], max_r[i]) - height[i]
            if water > 0:
                result += water

        return result
        