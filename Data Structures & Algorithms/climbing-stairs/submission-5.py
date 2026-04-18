class Solution:
    
    def climbStairs(self, n: int) -> int:
        values = [1,2]
        for i in range(2, n + 1):
            
            res = values[i - 1] + values[i - 2]
            print(res)
            values.append(res)
        
        return values[n - 1]

        
        