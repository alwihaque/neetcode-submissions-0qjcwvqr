class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        stack = []

        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: 
                head = stack.pop(-1)
                index, height = head
                max_area = max(max_area, (head[1] * (i - index)))
                start = index
            stack.append((start, h))
        for val in stack:
            index, height = val
            max_area = max(max_area, (height * (len(heights) - index)))
        return max_area
        