class Solution:
    
    


    def evalRPN(self, tokens: List[str]) -> int:
        def add(num_1, num_2):
            return num_1 + num_2
    
        def subtract(num_1, num_2):
            return num_1 - num_2
    
        def multiply(num_1, num_2):
            return num_1 * num_2
    
        def divide(num_1, num_2):
            return int(num_1 / num_2)
        operations = {
            '*': multiply,
            '+': add,
            '-': subtract,
            '/': divide
        }
        stack = []
        
        for i in tokens:
            if i not in operations.keys():
                stack.append(i)
            else:
                operator = i
                num_2 = int(stack.pop())
                num_1 = int(stack.pop())
                result = operations[i](num_1, num_2)
                stack.append(str(result))
        
        return int(stack[-1])



                        
        