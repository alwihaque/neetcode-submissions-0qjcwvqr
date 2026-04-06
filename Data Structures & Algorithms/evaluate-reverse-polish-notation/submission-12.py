class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def multiply(a, b):
            return a * b
        def divide(a, b):
            return int(a / b)
        def add(a, b):
            return a + b
        def subtract(a,b):
            return a - b        
        stack = []
        operators = "*-+/"
        operators = {
            '*': multiply,
            '/': divide,
            '+': add,
            '-': subtract
        }

        for c in tokens:
            print(stack)
            if c not in operators:
                stack.append(c)
            else:
                val_1 = int(stack.pop(-1))
                val_2 = int(stack.pop(-1))
                res = operators[c](val_2, val_1)
                stack.append(str(res))

        return int(stack[-1]) 
        