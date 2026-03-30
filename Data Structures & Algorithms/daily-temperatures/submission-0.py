class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        stack.append([temperatures[0],0])
        for index,temp in enumerate(temperatures):
            # check top of stack
            while len(stack) > 0 and stack[-1][0] < temp:
                elem = stack.pop(-1)
                difference = index - elem[1]
                res[elem[1]] = difference 
            stack.append([temp, index])
        
        # for elements in the stack still present no days were found

        # while len(stack) > 0:
        #     elem = stack.pop(-1)
        #     res[elem[1]] = 0
        
        return res
        

                


            
        