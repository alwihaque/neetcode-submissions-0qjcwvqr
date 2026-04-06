class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            
            if not stack or temp < stack[-1][0]:
                stack.append((temp, i))
            else:
                while stack and stack[-1][0] < temp:
                    _, index = stack.pop(-1)
                    res[index] = i - index
                
                stack.append((temp, i))
        
        while stack:
            _, index = stack.pop(-1)
            res[index] = 0
        
        return res
            
        